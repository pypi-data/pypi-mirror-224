#!/usr/bin/env python
import os

from botrun_embeddings import create_embeddings, find_similar_files
from botrun_pdf_to_text import botrun_pdf_to_text_single_file
from call_openai_gpt import call_openai_gpt


def botrun_pdf_qa_single_file(file_path: str, question: str, model="gpt-3.5-turbo-16k", top_k=10):
    botrun_pdf_to_text_single_file(file_path)
    base_path, _ = os.path.splitext(file_path)
    create_embeddings(base_path)
    similar_files_str = find_similar_files(question, base_path, top_k=top_k)
    p = f'''
    ### 知識庫內容:
        {similar_files_str}
    ### 回答時注意:
        須附註顯示引用了哪些文件名稱的哪些頁數(可精確指出上半部或下半部)
    ### 使用者提問:{question}
    '''
    return call_openai_gpt(p, model=model)


if __name__ == "__main__":
    ai_answer = botrun_pdf_qa_single_file("./users/cbh_cameo_tw/data/upload_files/222715345.pdf",
                                          "主管的男女比例是多少，還有土木工程技師男女比例")
    print(ai_answer)
