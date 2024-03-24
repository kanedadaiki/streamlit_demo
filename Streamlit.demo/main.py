import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

# st.dataframe(df.style.highlight_max(axis=0), width=1000, height=1000)
# 上記は動的な表を作る際に用いる

# st.table(df.style.highlight_max(axis=0))
# 上記はソート機能のない表を用意する

# df = pd.DataFrame(
#     np.random.rand(100, 2),
#     columns=['a', 'b', 'c']
# )
# 上記はランダムな数を100行２列生成する

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
# 新宿付近の緯度経度にランダムな数を足したマッピング
st.map(df)
# 上記はマッピング


st.line_chart(df)
# 上記は折れ線グラフ

st.area_chart(df)
# 上記は折れ線グラフに色を塗ったもの

st.bar_chart(df)
# 上記は棒グラフ

# st.write('Display Image')
# Image.open('')
# st.iamge(caption='ishida', use_column_width=True)
# # 画像を入れる場合はこちら
"""
# 以下streamlit例
"""


"""
## 基本的な動的な表

```python
import streamlit as st
import numpy as np
import pandas pd

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})
```

"""

"""

## 画像を入れる場合はこちら

```python
st.write('Display Image')
Image.open('')
st.iamge(img, caption='', use_column_width=True)
```

"""