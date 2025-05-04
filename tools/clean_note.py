import nbformat

# 读取上传的 Notebook 文件
notebook_path = '../deeplearning-ai/Tensorflow-C3-NLP.ipynb'  # 上传后的文件路径
with open(notebook_path, 'r') as f:
    notebook = nbformat.read(f, as_version=4)

# 清理 widgets metadata
for cell in notebook.cells:
    if 'metadata' in cell and 'widgets' in cell.metadata:
        del cell.metadata['widgets']

# 保存清理后的 Notebook
cleaned_notebook_path = notebook_path
with open(cleaned_notebook_path, 'w') as f:
    nbformat.write(notebook, f)

print(f"Cleaned notebook saved at: {cleaned_notebook_path}")