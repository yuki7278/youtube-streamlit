import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit入門')

st.write('DetaFrame')

df= pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})
st.write(df)
st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)

# st.table(df.style.highlight_max(axis=0))

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.area_chart(df2)
st.area_chart(df2)


df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df3)


st.write('Display Image')

if st.checkbox('Show Image'):
    img=Image.open('screenshot.jpg')
    st.image(img, caption='Screenshot', use_column_width=True)


option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11))
)

'あなたの好きな数字は、', option, 'です。'

st.write('Interactive Widgets')

# left_column, right_column = st.beta_colums(2) 　※現在は’beta_’無
# left_column.button('右カラムに文字を表示')
# if botton:
#     right_column.write('ここは右カラム')

# expander = st.beta_expander('問い合わせ')
# expander.write('問い合わせ内容を書く')

text = st.text_input('あなたの趣味を教えて下さい。')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味は、', text
'コンディション：', condition

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""


st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!!'


