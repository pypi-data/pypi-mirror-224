import os
import fitz
import glob
import pandas as pd
import re
from google.cloud import vision
import io
import numpy as np
from datetime import datetime

def extract_data_digital(invoice_file_path):
    doc = None
    with fitz.open(invoice_file_path) as doc:
        df = pd.DataFrame()
        counter = 0
        for d in doc:
            counter+=1
            pdf_data = d.get_text('words')
            x = []
            y = []
            w = []
            h = []
            word = []
            for line in pdf_data:
                line_split = line
                x.append(line_split[0])
                y.append(line_split[1])
                w.append(line_split[2])
                h.append(line_split[3])
                word.append(line_split[4])
            df_page = pd.DataFrame()
            df_page['x'] = x
            df_page['y'] = y
            df_page['w'] = w
            df_page['h'] = h
            df_page['output'] = word
            df_page[['x', 'y', 'w', 'h']] = df_page[['x', 'y', 'w', 'h']].astype(float)
            word = [re.sub(r'\s+', '', words) for words in word]
            word = [re.sub(r'^_+$', '', words) for words in word]
            word = [re.sub(r'^[\-]{2,}$', '', words) for words in word]
            word = [re.sub(r'^\*+$', '', words) for words in word]
            word = [re.sub(r'^\~+$', '', words) for words in word]
            word = [re.sub(r'^\|+$', '', words) for words in word]
            df_page["output"] = word
            df_page = df_page.reset_index(drop=True)
            df_page = df_page.sort_values(['y', 'x'])
            df_page.reset_index(inplace=True,drop=True)
            df_page['y_diff'] = df_page['y'] - df_page['y'].shift(1)
            df_page['median'] = (df_page['h']-df_page['y'])/2
            df_page['line_number'] = (df_page['median'].shift(1) < df_page['y_diff']).cumsum()
            df_page['page_number'] = counter
            df_page[['line_number', 'page_number']] = df_page[['line_number', 'page_number']].astype(int)
            page_text = ''.join(df_page['output'])
            if df.empty:
                df = df_page.copy()
            else:
                y_max_page = max(df['y'])
                h_max_page = max(df['h'])
                l_max_page = max(df['line_number'])
                df_page[['y']] = df_page[['y']]+y_max_page
                df_page[['h']] = df_page[['h']]+h_max_page
                df_page[['line_number']] = df_page[['line_number']]+l_max_page
                df = df.append(df_page, ignore_index=True)
    df['c'] = 100
    df = df.sort_values(['line_number', 'x'])
    df.reset_index(inplace=True,drop=True)
    return df

def extract_data_gcv(invoice_file_path, credential_file):
    credential_file_path = credential_file
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_file_path
    client = vision.ImageAnnotatorClient()
    user_profile = os.environ['USERPROFILE']
    documents_path = os.path.join(user_profile, 'Documents', 'invoiceimages')
    dir_exist = os.path.exists(documents_path)
    if not dir_exist:
        os.makedirs(documents_path)
    file_list = glob.glob(documents_path + '\\*.png')
    for f in file_list:
        os.remove(f)
    image_file_path = os.path.join(documents_path, 'invoice.png')
    doc = None
    with fitz.open(invoice_file_path) as doc:
        df = pd.DataFrame()
        counter = 0
        for d in doc:
            counter+=1
            page = d
            image_matrix = fitz.Matrix(fitz.Identity)
            image_matrix.preScale(3, 3)
            pix = page.getPixmap(alpha=False, matrix=image_matrix)
            pix.writePNG(image_file_path)
            with io.open(image_file_path, 'rb') as img_file:
                content = img_file.read()
            image = vision.types.Image(content=content)
            response = client.text_detection(image=image)
            output_text = response.full_text_annotation
            x = []
            y = []
            w = []
            h = []
            c = []
            text_output = []
            for page in output_text.pages:
                for block in page.blocks:
                    for paragraph in block.paragraphs:
                        try:
                            conf_prop = paragraph.property.detected_languages[0].confidence
                            conf_prop = int(round(conf_prop*100))
                        except:
                            conf_prop = 100
                        words = []
                        for word in paragraph.words:
                            for symbol in word.symbols:
                                words.append(symbol.text)
                            output_word = ''.join(words)
                            text_output.append(output_word)
                            c.append(conf_prop)
                            x_val = word.bounding_box.vertices[0].x
                            y_val = word.bounding_box.vertices[0].y
                            x1 = word.bounding_box.vertices[1].x
                            y1 = word.bounding_box.vertices[2].y
                            w_val = abs(x_val-x1)
                            h_val = abs(y_val-y1)
                            x.append(x_val)
                            y.append(y_val)
                            w.append(w_val)
                            h.append(h_val)
                            words = []
            df_page = pd.DataFrame()
            df_page['x'] = x
            df_page['y'] = y
            df_page['w'] = w
            df_page['h'] = h
            df_page['c'] = c
            df_page['output'] = text_output
            df_page[['x', 'y', 'w', 'h']] = df_page[['x', 'y', 'w', 'h']].astype(float)
            text_output = [re.sub(r'\s+', ' ', words) for words in text_output]
            text_output = [re.sub(r'^_+$', '', words) for words in text_output]
            text_output = [re.sub(r'^[\-]{2,}$', '', words) for words in text_output]
            text_output = [re.sub(r'^\*+$', '', words) for words in text_output]
            text_output = [re.sub(r'^\~+$', '', words) for words in text_output]
            text_output = [re.sub(r'^\|+$', '', words) for words in text_output]
            df_page["output"] = text_output
            df_page = df_page.reset_index(drop=True)
            df_page = df_page.sort_values(['y', 'x'])
            df.reset_index(inplace=True,drop=True)
            df_page['y_diff'] = df_page['y'] - df_page['y'].shift(1)
            df_page['median'] = df_page['h']/2
            df_page['line_number'] = (df_page['median'].shift(1) < df_page['y_diff']).cumsum()
            df_page['page_number'] = counter
            df_page[['line_number', 'page_number']] = df_page[['line_number', 'page_number']].astype(int)
            page_text = ''.join(df_page['output'])
            if not ('typestandardpurchaseorder' in page_text.lower()):
                if df.empty:
                    df = df_page.copy()
                else:
                    y_max_page = max(df['y'])
                    df_page[['y']] = df_page[['y']]+y_max_page
                    l_max_page = max(df['line_number'])
                    df_page[['line_number']] = df_page[['line_number']]+l_max_page+1
                    df = df.append(df_page, ignore_index=True)
    df = df.sort_values(['line_number', 'x'])
    df.reset_index(inplace=True,drop=True)
    df['w'] = df['x']+df['w']
    df['h'] = df['y']+df['h']
    return df


def combine_line_wise_data(df):
    line_numbers = df['line_number'].unique()
    lines_data = []
    
    for line in line_numbers:
        line_df = df[df['line_number']==line]
        line_df = line_df.sort_values(by='x')
        lines_data.append("".join(list(line_df['output'])))
    return lines_data

def extract_invoice_field_values(invoice_df, lines, template_df, ocr_type, field_identifier_duplicate = ''):
    confidence_score = 100
    columns = template_df['OUTPUT_LABEL'].tolist()
    rows = []
    output_values = []
    for ind in template_df.index:
        output_value = 'not found'
        output_label = str(template_df['OUTPUT_LABEL'][ind]).strip().lower().replace(' ', '')
        label_name = str(template_df['LABEL'][ind]).strip().lower().replace(' ', '')
        reference_position = str(template_df['REF_POSITION'][ind]).strip().lower().replace(' ', '')
        top_ref_label_name = str(template_df['TOP_REF'][ind]).strip().lower().replace(' ', '')
        top_limiting_position = 0
        top_line_number = 0
        top_ref_alighnment = str(template_df['TOP_REF_ALIGN'][ind]).strip().lower()
        bottom_ref_label_name = str(template_df['BOTTOM_REF'][ind]).strip().lower().replace(' ', '')
        bottom_ref_alighnment = str(template_df['BOTTOM_REF_ALIGN'][ind]).strip().lower()
        bottom_limiting_position = max(invoice_df['h'])+10
        bottom_line_number = max(invoice_df['line_number'])
        left_ref_label_name = str(template_df['LEFT_REF'][ind]).strip().lower().replace(' ', '')
        left_ref_alighnment = str(template_df['LEFT_REF_ALIGN'][ind]).strip().lower()
        left_limiting_position = 0
        right_ref_label_name = str(template_df['RIGHT_REF'][ind]).strip().lower().replace(' ', '')
        right_ref_alighnment = str(template_df['RIGHT_REF_ALIGN'][ind]).strip().lower()
        right_limiting_position = max(invoice_df['w'])+10
        is_paragraph = str(template_df['IS_PARAGRAPH'][ind]).lower()
        max_number_of_lines = template_df['MAX_NUMBER_OF_LINES'][ind]
        date_format = str(template_df['DATE_FORMAT'][ind]).strip()
        if ocr_type == 'digital':
            left_x = template_df['LEFT_X_DIGITAL'][ind]
            right_x = template_df['RIGHT_X_DIGITAL'][ind]
        else:
            left_x = template_df['LEFT_X'][ind]
            right_x = template_df['RIGHT_X'][ind]
        if left_x == np.nan:
            left_x = 0
        if right_x == np.nan:
            right_x=0
        value_type = str(template_df['VALUE_TYPE'][ind]).lower()
        pattern = str(template_df['PATTERN'][ind])
        
        
        
        if label_name.lower() == 'na':
            output_value = 'na'
        elif reference_position.lower() == 'self':
            output_value = str(template_df['LABEL'][ind])
        else:
            #calculate top limiting position
            top_ref_label_found = False
            if not(top_ref_label_name == 'na' or top_ref_label_name == 'nan' or top_ref_label_name == 'end'):
                
                for line in lines:
                    if top_ref_label_name in line.lower().replace(' ', ''):
                        line_index = lines.index(line)
                        top_line_number = line_index
                        if line_index == max(invoice_df['line_number']):
                            next_line_index = line_index
                        else:
                            next_line_index = line_index+1
                        top_ref_df = invoice_df[invoice_df['line_number'] == line_index]
                        top_next_df = invoice_df[invoice_df['line_number'] == next_line_index]
                        top_ref_label_found = True
                        break
                if top_ref_label_found:
                    if top_ref_alighnment == 'top':
                        top_limiting_position = min(top_ref_df['y'])-2
                    elif top_ref_alighnment == 'centre':
                        top_limiting_position = (max(top_ref_df['h'])+min(top_ref_df['y']))/2
                    else:
                        top_line_number = top_line_number+1
                        top_limiting_position = min(top_next_df['y'])-2
                else:
                    pass
            #calculate bottom limiting position
            bottom_ref_label_found = False
            if not(bottom_ref_label_name == 'na' or bottom_ref_label_name == 'nan' or bottom_ref_label_name == 'end'):
                
                for line in lines:
                    if bottom_ref_label_name in line.lower().replace(' ', ''):
                        line_index = lines.index(line)
                        if line_index>=top_line_number:
                            bottom_line_number = line_index
                            if line_index == max(invoice_df['line_number']):
                                next_line_index = line_index
                            else:
                                next_line_index = line_index+1
                            bottom_ref_df = invoice_df[invoice_df['line_number'] == line_index]
                            bottom_next_df = invoice_df[invoice_df['line_number'] == next_line_index]
                            bottom_ref_label_found = True
                            break
                if bottom_ref_label_found:
                    if bottom_ref_alighnment == 'bottom':
                        bottom_limiting_position = min(bottom_next_df['y'])-2
                    elif bottom_ref_alighnment == 'centre':
                        bottom_limiting_position = (max(bottom_ref_df['h'])+min(bottom_ref_df['y']))/2
                    else:
                        bottom_line_number = bottom_line_number-1
                        bottom_limiting_position = min(bottom_ref_df['y'])-2
                else:
                    pass
            #calculate left limiting position
            left_ref_label_found = False
            if not(left_ref_label_name == 'na' or left_ref_label_name == 'nan' or left_ref_label_name == 'end'):
                
                for line in lines:
                    if left_ref_label_name in line.lower().replace(' ', ''):
                        line_index = lines.index(line)
                        left_ref_df = invoice_df[invoice_df['line_number'] == line_index]
                        first_char = line.lower().find(left_ref_label_name)
                        last_char = first_char+len(left_ref_label_name)
                        left_ref_df = left_ref_df.reset_index(drop = True)
                        count = 0
                        x = min(left_ref_df['x'])
                        w = max(left_ref_df['w'])
                        for ind_sub in left_ref_df.index:
                            if ind_sub == len(left_ref_df)-1:
                                next_index = ind_sub
                            else:
                                next_index = ind_sub+1
                            val = left_ref_df['output'][ind_sub]
                            count = count+len(val)
                            if first_char == 0:
                                x = min(left_ref_df['x'])
                            elif first_char == count:
                                x = left_ref_df['x'][next_index]
                            if last_char <= count:
                                w = left_ref_df['w'][ind_sub]
                                break
                        left_ref_label_found = True
                        break
                if left_ref_label_found:
                    if left_ref_alighnment == 'left':
                        left_limiting_position = x
                    elif left_ref_alighnment == 'centre':
                        left_limiting_position = (x+w)/2
                    else:
                        left_limiting_position = w
                else:
                    pass
            #calculate right limiting position
            right_ref_label_found = False
            if not(right_ref_label_name == 'na' or right_ref_label_name == 'nan' or right_ref_label_name == 'end'):
                
                for line in lines:
                    if right_ref_label_name in line.lower().replace(' ', ''):
                        line_index = lines.index(line)
                        right_ref_df = invoice_df[invoice_df['line_number'] == line_index]
                        first_char = line.lower().find(right_ref_label_name)
                        last_char = first_char+len(right_ref_label_name)
                        right_ref_df = right_ref_df.reset_index(drop = True)
                        count = 0
                        x = min(right_ref_df['x'])
                        w = max(right_ref_df['w'])
                        for ind_sub in right_ref_df.index:
                            if ind_sub == len(right_ref_df)-1:
                                next_index = ind_sub
                            else:
                                next_index = ind_sub+1
                            val = right_ref_df['output'][ind_sub]
                            count = count+len(val)
                            if first_char == 0:
                                x = min(right_ref_df['x'])
                            elif first_char == count:
                                x = right_ref_df['x'][next_index]
                            if last_char <= count:
                                w = right_ref_df['w'][ind_sub]
                                break
                        right_ref_label_found = True
                        break
                if right_ref_label_found:
                    if right_ref_alighnment == 'right':
                        right_limiting_position = w
                    elif right_ref_alighnment == 'centre':
                        right_limiting_position = (x+w)/2
                    else:
                        right_limiting_position = x
                else:
                    pass
            label_name_found = False
            label_ref_df = pd.DataFrame()
            if not label_name == 'nan':
                for line in lines:
                    if label_name in line.lower():
                        label_line_number = lines.index(line)
                        if (label_line_number>=top_line_number) & (label_line_number<=bottom_line_number):
                            
                            label_ref_df = invoice_df[invoice_df['line_number'] == label_line_number]
                            first_char = line.lower().find(label_name)
                            last_char = first_char+len(label_name)
                            label_ref_df = label_ref_df.reset_index(drop = True)
                            count = 0
                            label_left = min(label_ref_df['x'])
                            label_right = max(label_ref_df['w'])
                            for ind_sub in label_ref_df.index:
                                if ind_sub == len(label_ref_df)-1:
                                    next_index = ind_sub
                                else:
                                    next_index = ind_sub+1
                                val = label_ref_df['output'][ind_sub]
                                count = count+len(val)
                                if first_char == 0:
                                    label_left = min(label_ref_df['x'])
                                elif first_char == count:
                                    label_left = label_ref_df['x'][next_index]
                                if last_char <= count:
                                    label_right=label_ref_df['w'][ind_sub]
                                    break
                            label_name_found=True
                            break
            else:
                pass
            
            value_df = pd.DataFrame()
            if max_number_of_lines == np.nan:
                max_number_of_lines = 1
            if label_name_found:            
                if reference_position == 'right':
                    if top_ref_label_name == 'na' and bottom_ref_label_name == 'na':
                        value_df = invoice_df[(invoice_df['line_number']==label_line_number) & (invoice_df['x']>=label_right-left_x) & (invoice_df['w']<=right_limiting_position+right_x)]
                    else:
                        value_df = invoice_df[(invoice_df['line_number']>=label_line_number)&(invoice_df['x']>=label_right-left_x)&(invoice_df['w']<=right_limiting_position+right_x)&(invoice_df['y']>=top_limiting_position)&(invoice_df['y']<=bottom_limiting_position)]
                elif reference_position == 'below':
                    if right_ref_label_name == 'na' or right_ref_label_name == 'nan':
                        right_limiting_position = label_right+right_x
                    if left_ref_label_name == 'na' or left_ref_label_name == 'nan':
                        left_limiting_position = label_left-left_x
                    value_df = invoice_df[(invoice_df['line_number']>=label_line_number+1)&(invoice_df['x']>=left_limiting_position)&(invoice_df['w']<=right_limiting_position)&(invoice_df['h']<=bottom_limiting_position)]
                    
                elif reference_position == 'above':
                    left_limiting_position = left_limiting_position-left_x
                    right_limiting_position = right_limiting_position+right_x
                    value_df = invoice_df[(invoice_df['line_number']<=label_line_number)&(invoice_df['x']>=left_limiting_position)&(invoice_df['w']<=right_limiting_position)&(invoice_df['y']<=bottom_limiting_position)&(invoice_df['y']>=top_limiting_position)]
                elif reference_position == 'left':
                    pass
            else:
                if reference_position == 'right':
                    pass
                elif reference_position == 'below':
                    pass
                elif reference_position == 'above':
                    pass
                elif reference_position == 'left':
                    pass
            if(len(value_df) == 0):
                output_value = ''
            else:
                value_df = value_df.reset_index(drop=True)
                l_no = value_df['line_number'][0]+max_number_of_lines-1
                final_val_df = value_df [ value_df['line_number']<=l_no]
                if (len(final_val_df)>0):
                    field_confidence_score = min(final_val_df['c'])
                if field_confidence_score<confidence_score:
                    confidence_score = field_confidence_score
                if is_paragraph=='yes':
                    minline = min(final_val_df['line_number'])
                    maxline = max(final_val_df['line_number'])
                    for lNo in range(minline, maxline+1):
                        line_df = final_val_df[final_val_df['line_number']==lNo]
                        lineoutput = ' '.join((list(line_df['output'])))
                        if lNo==minline:
                            output_value = lineoutput
                        else:
                            output_value = output_value+'\n'+lineoutput
                else:
                    output_value = ' '.join((list(final_val_df['output'])))
        if value_type == 'pattern':
            value_match = re.findall(pattern,output_value)
            if len(value_match)>0:
                output_value = value_match[0]
            else:
                output_value = 'not found'
        if field_identifier_duplicate == str(template_df['OUTPUT_LABEL'][ind]).strip():
            invoiceText = ''.join(list(lines))
            label_match = re.findall(str(template_df['LABEL'][ind]).strip().lower().replace(' ', ''), invoiceText.lower().replace(' ', ''))
            output_match = re.findall(output_value.lower().replace(' ', ''), invoiceText.lower().replace(' ', '') )
            if reference_position.strip().lower() == 'self':
                if len(label_match)>1:
                    raise AssertionError('File contains more than one invoice.')
            else:
                if len(label_match) != len(output_match):
                    raise AssertionError('File contains more than one invoice.')
        if 'date' in output_label.lower():
            if date_format == '' or date_format == 'na':
                output_values.append(output_value.strip())
            else:
                try:
                    date_obj = datetime.strptime(output_value.strip(), date_format)
                    date_value = datetime.strftime(date_obj, '%d-%b-%Y')
                    output_values.append(date_value.strip())
                except:
                    output_values.append(output_value.strip())
        else:
            output_values.append(output_value.strip())
    
    rows.append(output_values)
    invoice_header_df = pd.DataFrame(rows, columns = columns)
    return invoice_header_df, confidence_score

def extract_invoice_lineitems(invoice_df,lines,template_df, ocr_type):
    confidence_score = 100
    invoice_table_df = pd.DataFrame()
    Columns_names = template_df['COLUMN_NAME'].tolist()
    try:
        footer_optional = str(template_df['FOOTER_OPTIONAL'][0]).lower()
    except:
        footer_optional = 'no'
    try:
        header_topreference = str(template_df['HEADER_TOPREFERENCE'][0]).lower().replace(' ','')
    except:
        header_topreference = 'na'
    if header_topreference == 'na':
        header_topLine = 0
    else:
        for line in lines:
            found_topline = re.findall(header_topreference,line.lower().replace(' ',''))
            if len(found_topline)>0:
                header_topLine=lines.index(line)
                break
    Col_lineNumber = 0
    tableFirstLine = ""
    footer_line_number = 0
    col_label_list = template_df["COLUMN_LABEL"].tolist()
    col_label_list_new = []
    for col in col_label_list:
        col = col.replace('(','[(]').replace(')','[)]')
        col = col.lower().strip().replace(' ', '')
        if col == 'notfound' or col == 'na':
            pass
        else:
            col_label_list_new.append(col)
    pattern = ('|'.join(col_label_list_new))
    for line in lines:
        found_cols = re.findall(pattern, line.lower().replace(' ',''))
        if len(found_cols) >=3 or len(found_cols) == len(col_label_list_new):
            Col_lineNumber = lines.index(line)
            tableFirstLine = line.lower()
            if Col_lineNumber>header_topLine:
                break
    if Col_lineNumber == 0:
        raise AssertionError('Tabel header not found')
    row_ref_column_df = template_df[template_df["IS_REF_ROW"]=="Yes"].reset_index(drop=True)
    row_ref_column_label = row_ref_column_df["COLUMN_LABEL"][0].lower().strip().replace(' ','')
    col_spread = int(template_df['COL_SPREAD'][0])
    table_footer_label = str(template_df['TABLE_FOOTER'][0]).lower().strip().replace(' ','')
    if table_footer_label == 'na':
        footer_line_number = max(invoice_df['line_number']+1)
    else:
        for line in lines:
            found_footer = re.findall(table_footer_label,line.lower().replace(' ',''))
            if len(found_footer)>0:
                if lines.index(line)>Col_lineNumber:
                    footer_line_number = lines.index(line)
                    break
    if footer_optional == 'no':
        if footer_line_number == 0:
            raise AssertionError('Tabel footer not found')
    else:
        if footer_line_number == 0:
            footer_line_number = max(invoice_df['line_number']+1)
    column_df = invoice_df[(invoice_df['line_number']>(Col_lineNumber-1)) & (invoice_df['line_number']<(Col_lineNumber+col_spread))]
    column_df = column_df.reset_index(drop = True)
    ref_col_left_x = 0
    ref_col_right_x = max(invoice_df['h'])+100
    if row_ref_column_label == 'notfound':
        left_identifier = str(row_ref_column_df['LEFT_REF'][0]).lower().strip().replace(' ','')
        right_identifier = str(row_ref_column_df['RIGHT_REF'][0]).lower().strip().replace(' ','')
        if left_identifier == 'end':
            pass
        else:
            for line in lines:
                if left_identifier in line.lower():
                    line_number = lines.index(line)
                    line_df = invoice_df[invoice_df['line_number'] == line_number]
                    line_df = line_df.reset_index(drop = True)
                    last_char = line.lower().find(left_identifier) + len(left_identifier)
                    count = 0
                    for ind_sub in line_df.index:
                        val = line_df['output'][ind_sub]
                        count = count+len(val)
                        if last_char <= count:
                            if ocr_type == 'digital':
                                ref_col_left_x = line_df['w'][ind_sub] - row_ref_column_df['LEFT_X_DIGITAL'][0]
                            else:
                                ref_col_left_x = line_df['w'][ind_sub] - row_ref_column_df['LEFT_X'][0]
                            break
                    break
        if right_identifier == 'end':
            pass
        else:
            for line in lines:
                if right_identifier in line.lower():
                    line_number = lines.index(line)
                    line_df = invoice_df[invoice_df['line_number'] == line_number]
                    line_df = line_df.reset_index(drop = True)
                    first_char = line.lower().find(right_identifier)
                    count = 0
                    for ind_sub in line_df.index:
                        if ind_sub == len(line_df)-1:
                            next_index = ind_sub
                        else:
                            next_index = ind_sub+1
                        val = line_df['output'][ind_sub]
                        count = count+len(val)
                        if first_char == 0:
                            ref_col_right_x = min(line_df['x'])
                        elif first_char == count:
                            if ocr_type == 'digital':
                                ref_col_right_x = column_df['w'][ind_sub] + row_ref_column_df['RIGHT_X_DIGITAL'][0]
                            else:
                                ref_col_right_x = line_df['x'][next_index] + row_ref_column_df['RIGHT_X'][0]
                    break
    else:
        first_char = tableFirstLine.find(row_ref_column_label)      
        last_char = first_char+len(row_ref_column_label)
        count = 0
        ref_col_left_x = min(column_df['x'])
        ref_col_right_x = max(column_df['w'])
        for ind_sub in column_df.index:
            if ind_sub == len(column_df)-1:
                next_index = ind_sub
            else:
                next_index = ind_sub+1
            val = column_df['output'][ind_sub]
            count = count+len(val)
            if first_char == 0:
                if ocr_type == 'digital':
                    ref_col_left_x = min(column_df['x']) - row_ref_column_df['LEFT_X_DIGITAL'][0]
                else:
                    ref_col_left_x = min(column_df['x']) - row_ref_column_df['LEFT_X'][0]
            elif first_char == count:
                if ocr_type == 'digital':
                    ref_col_left_x = column_df['x'][next_index] - row_ref_column_df['LEFT_X_DIGITAL'][0]
                else:
                    ref_col_left_x = column_df['x'][next_index] - row_ref_column_df['LEFT_X'][0]
            if last_char <= count:
                if ocr_type == 'digital':
                    ref_col_right_x = column_df['w'][ind_sub] + row_ref_column_df['RIGHT_X_DIGITAL'][0]
                else:
                    ref_col_right_x = column_df['w'][ind_sub] + row_ref_column_df['RIGHT_X'][0]
                break
    row_ref_df = invoice_df[(invoice_df['line_number']>=(Col_lineNumber+col_spread)) & (invoice_df['line_number']<footer_line_number) &(invoice_df['x']>=ref_col_left_x) &(invoice_df['w']<=ref_col_right_x)]
    row_lineNumbers = row_ref_df.line_number.unique()
    tabel_values = []
    
    if template_df['REF_ALIGN'][0].upper() == "TOP":
        for i in range(0,len(row_lineNumbers)):
            row_values = []
            if i == len(row_lineNumbers)-1:
                firstline = row_lineNumbers[i]
                nextline = footer_line_number
            else:
                firstline = row_lineNumbers[i]
                nextline = row_lineNumbers[i+1]
                
            for ind in template_df.index:
                label = template_df['COLUMN_LABEL'][ind].lower().strip().replace(' ','')
                if ocr_type == 'digital':
                    template_left_x = template_df['LEFT_X_DIGITAL'][ind]
                    template_right_x = template_df['RIGHT_X_DIGITAL'][ind]
                else:
                    template_left_x = template_df['LEFT_X'][ind]
                    template_right_x = template_df['RIGHT_X'][ind]
                if template_left_x == np.nan:
                    template_left_x = 0
                if template_right_x == np.nan:
                    template_right_x=0
                if label == 'na':
                    value = ''
                else:
                    left_x = 0
                    right_x = max(invoice_df['w'])+100
                    if label == 'notfound':
                        left_identifier = template_df['LEFT_REF'][ind].lower().strip().replace(' ','')
                        right_identifier = template_df['RIGHT_REF'][ind].lower().strip().replace(' ','')
                        if left_identifier == 'end':
                            pass
                        else:
                            for line in lines:
                                if left_identifier in line.lower():
                                    line_number = lines.index(line)
                                    line_df = invoice_df[invoice_df['line_number'] == line_number]
                                    line_df = line_df.reset_index(drop = True)
                                    last_char = line.lower().find(left_identifier) + len(left_identifier)
                                    count = 0
                                    for ind_sub in line_df.index:
                                        val = line_df['output'][ind_sub]
                                        count = count+len(val)
                                        if last_char <= count:
                                            left_x = line_df['w'][ind_sub]-template_left_x
                                            break
                                    break
                        if right_identifier == 'end':
                            right_x = max(invoice_df['w'])+100
                        else:
                            for line in lines:
                                if right_identifier in line.lower():
                                    line_number = lines.index(line)
                                    line_df = invoice_df[invoice_df['line_number'] == line_number]
                                    line_df = line_df.reset_index(drop = True)
                                    first_char = line.lower().find(right_identifier)
                                    count = 0
                                    for ind_sub in line_df.index:
                                        if ind_sub == len(line_df)-1:
                                            next_index = ind_sub
                                        else:
                                            next_index = ind_sub+1
                                        val = line_df['output'][ind_sub]
                                        count = count+len(val)
                                        if first_char == 0:
                                            right_x = min(line_df['x']) + template_right_x
                                        elif first_char == count:
                                            right_x = line_df['x'][next_index] + template_right_x
                                    break
                    else:                
                        first_char = tableFirstLine.find(label)       
                        last_char = first_char+len(label)
                        count = 0
                        left_x = 0
                        right_x = max(column_df['w'])
                        for ind_sub in column_df.index:
                            if ind_sub == len(column_df)-1:
                                next_index = ind_sub
                            else:
                                next_index = ind_sub+1
                            val = column_df['output'][ind_sub]
                            count = count+len(val)
                            if first_char == 0:
                                left_x = min(column_df['x']) - template_left_x
                            elif first_char == count:
                                left_x = column_df['x'][next_index] - template_left_x
                            if last_char <= count:
                                right_x = column_df['w'][ind_sub]+template_right_x
                                break
                    row_value_df = invoice_df[(invoice_df['line_number']>=firstline) & (invoice_df['line_number']<nextline) &(invoice_df['x']>left_x) &(invoice_df['w']<right_x)]
                    value = ' '.join((list(row_value_df['output'])))
                    if len(row_value_df)==0:
                        pass
                    else:
                        field_confidence_score = min(row_value_df['c'])
                        if field_confidence_score<confidence_score:
                            confidence_score = field_confidence_score
                try:
                    pattern = template_df['PATTERN'][ind]
                    if pattern.strip().lower() == 'na' or pattern.strip() == '':
                        output_value = value
                    else:
                        value_match = re.findall(pattern,value)
                        if len(value_match)>0:
                            output_value = value_match[0]
                        else:
                            output_value = ''
                except Exception as e:
                    output_value = value
                row_values.append(output_value)
            tabel_values.append(row_values)
        invoice_table_df = pd.DataFrame(tabel_values, columns = Columns_names)
    if template_df['REF_ALIGN'][0].upper() == "BOTTOM":
        for i in range(0,len(row_lineNumbers)):
            row_values = []
            if i == 0:
                firstline = Col_lineNumber+col_spread
                nextline = row_lineNumbers[i]+1
            else:
                firstline = row_lineNumbers[i-1]+1
                nextline = row_lineNumbers[i]+1
            for ind in template_df.index:
                label = template_df['COLUMN_LABEL'][ind].lower().strip().replace(' ','')
                if ocr_type == 'digital':
                    template_left_x = template_df['LEFT_X_DIGITAL'][ind]
                    template_right_x = template_df['RIGHT_X_DIGITAL'][ind]
                else:
                    template_left_x = template_df['LEFT_X'][ind]
                    template_right_x = template_df['RIGHT_X'][ind]
                if template_left_x == np.nan:
                    template_left_x = 0
                if template_right_x == np.nan:
                    template_right_x=0
                if label == 'na':
                    value = ''
                else:
                    left_x = 0
                    right_x = max(invoice_df['h'])+100
                    if label == 'notfound':
                        left_identifier = template_df['LEFT_REF'][ind].lower().strip().replace(' ','')
                        right_identifier = template_df['RIGHT_REF'][ind].lower().strip().replace(' ','')
                        if left_identifier.lower() == 'end':
                            pass
                        else:
                            for line in lines:
                                if left_identifier in line.lower():
                                    line_number = lines.index(line)
                                    line_df = invoice_df[invoice_df['line_number'] == line_number]
                                    line_df = line_df.reset_index(drop = True)
                                    last_char = line.lower().find(left_identifier) + len(left_identifier)
                                    count = 0
                                    for ind_sub in line_df.index:
                                        val = line_df['output'][ind_sub]
                                        count = count+len(val)
                                        if last_char <= count:
                                            left_x = line_df['w'][ind_sub]-template_left_x
                                            break
                                    break
                        if right_identifier.lower() == 'end':
                            pass
                        else:
                            for line in lines:
                                if right_identifier in line.lower():
                                    line_number = lines.index(line)
                                    line_df = invoice_df[invoice_df['line_number'] == line_number]
                                    line_df = line_df.reset_index(drop = True)
                                    first_char = line.lower().find(right_identifier)
                                    count = 0
                                    for ind_sub in line_df.index:
                                        if ind_sub == len(line_df)-1:
                                            next_index = ind_sub
                                        else:
                                            next_index = ind_sub+1
                                        val = line_df['output'][ind_sub]
                                        count = count+len(val)
                                        if first_char == 0:
                                            right_x = min(line_df['x']) + template_right_x
                                        elif first_char == count:
                                            right_x = line_df['x'][next_index] + template_right_x
                                    break
                    else:                
                        first_char = tableFirstLine.find(label)       
                        last_char = first_char+len(label)
                        count = 0
                        left_x = 0
                        right_x = max(column_df['w'])
                        for ind_sub in column_df.index:
                            if ind_sub == len(column_df)-1:
                                next_index = ind_sub
                            else:
                                next_index = ind_sub+1
                            val = column_df['output'][ind_sub]
                            count = count+len(val)
                            if first_char == 0:
                                left_x = min(column_df['x']) - template_left_x
                            elif first_char == count:
                                left_x = column_df['x'][next_index] - template_left_x
                            if last_char <= count:
                                right_x = column_df['w'][ind_sub] + template_right_x
                                break
                    row_value_df = invoice_df[(invoice_df['line_number']>=firstline) & (invoice_df['line_number']<nextline) &(invoice_df['x']>left_x) &(invoice_df['w']<right_x)]
                    value = ' '.join((list(row_value_df['output'])))
                    if len(row_value_df)==0:
                        pass
                    else:
                        field_confidence_score = min(row_value_df['c'])
                        if field_confidence_score<confidence_score:
                            confidence_score = field_confidence_score
                try:
                    pattern = template_df['PATTERN'][ind]
                    if pattern.strip().lower() == 'na' or pattern.strip() == '':
                        output_value = value
                    else:
                        value_match = re.findall(pattern,value)
                        if len(value_match)>0:
                            output_value = value_match[0]
                        else:
                            output_value = ''
                except Exception as e:
                    output_value = value
                row_values.append(output_value)
            tabel_values.append(row_values)
        invoice_table_df = pd.DataFrame(tabel_values, columns = Columns_names)
        
    for ind in template_df.index:
        columnName = template_df['COLUMN_NAME'][ind]
        labelName = template_df['COLUMN_LABEL'][ind]

        if columnName == 'line-no' and labelName.lower() == 'na':
            invoice_table_df['line-no'] = np.arange(len(invoice_table_df))
            invoice_table_df['line-no'] = invoice_table_df['line-no']+1
    try:
        quantity_unitprice_df = template_df[(template_df['COLUMN_NAME'] == 'unit-price') | (template_df['COLUMN_NAME'] == 'quantity')]
        quantity_unitprice_df.reset_index(inplace=True,drop=True)
        if (str(quantity_unitprice_df['COLUMN_LABEL'][0]).strip().lower() == 'na' or str(quantity_unitprice_df['COLUMN_LABEL'][0]).strip().lower() == '') and (str(quantity_unitprice_df['COLUMN_LABEL'][1]).strip().lower() == 'na' or str(quantity_unitprice_df['COLUMN_LABEL'][1]).strip().lower() == ''):
            invoice_table_df['unit-price'] = 1
            invoice_table_df['quantity'] = invoice_table_df['line-amount']
    except Exception as e:
        pass

    return invoice_table_df, confidence_score

