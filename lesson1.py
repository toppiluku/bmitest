import streamlit as st

st.set_page_config(page_title='BODY MASS INDEX')

st.title('BMI Calculator')
st.header('Input Your Weight and Height in Box!')

a = st.number_input('Weight(in Kg.)')
b = st.number_input('Height(in Cm.)')
res = st.empty()
if st.button('Calculate'):
    bm = a / ((b / 100) ** 2)
    st.write(f"BMI is {bm:.2f}")
    if bm > 30:
        st.error('Fat 3')
        res.image('fat1.png')
    elif bm >= 23:
        st.warning('Fat 1-2')
        res.image('fat2.png')
    elif bm >= 18.5:
        st.success('Normal')
        res.image('.png')
    else:
        st.info('Thin')
        res.image('thin.png')
