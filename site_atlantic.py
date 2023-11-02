import pandas as pd
import streamlit as st 
import numpy as np



st.header("Харчування 2023-2024 - листопад")
st.write(" ")
st.write("Загальна таблиця по харчуванню відображена нижче")
uploaded_file = st.file_uploader("Завантажити файл по харчуванню", type=['csv', 'txt'])
if uploaded_file is not None:
    # Читання файла, лише якщо файл був завантажений
    data = pd.read_csv(uploaded_file, encoding='utf-8', delimiter=',')
    st.write("Дані з файлу:")

    data['№'] = pd.to_numeric(data['№'], errors='coerce')
    processed_data = data['№'].dropna().astype(int)
    data.fillna(" ")
    data["№"] = processed_data
    #data = data.fillna(" ")
    st.write(data)

    st.write(" ")
    st.subheader("Напишіть дату для формування замовлення:")

    day_order = st.text_input("Поле для вводу:")
    # st.write(day_order)
    if day_order in data:
        desired_value = "сніданок"
        filtered_data = data[data.iloc[:, 1] == desired_value]
        unique_values_count = filtered_data[day_order].value_counts().reset_index()
        unique_values_count = pd.DataFrame(unique_values_count)
        unique_values_count1 = unique_values_count.rename(columns={day_order: 'Сніданок', 'count': 'Сніданок кількість'})
        st.write(" ")
        st.write("##### Сніданок за категоріями: ")
        st.dataframe(unique_values_count1 , width=800)


        desired_value = "обід"
        filtered_data = data[data.iloc[:, 1] == desired_value]
        unique_values_count = filtered_data[day_order].value_counts().reset_index()
        unique_values_count = pd.DataFrame(unique_values_count)
        unique_values_count2 = unique_values_count.rename(columns={day_order: 'Обід', 'count': 'Обід кількість'})
        st.write(" ")
        st.write("##### Обід за категоріями: ")
        st.dataframe(unique_values_count2, width=800)



        desired_value = "снек"
        filtered_data = data[data.iloc[:, 1] == desired_value]
        unique_values_count = filtered_data[day_order].value_counts().reset_index()
        unique_values_count = pd.DataFrame(unique_values_count)
        unique_values_count3 = unique_values_count.rename(columns={day_order: 'Снек категорії', 'count': 'Cнек кількість' })
        st.write(" ")
        st.write("##### Снек за категоріями: ")
        st.dataframe(unique_values_count3, width=800)

        desired_value = "вечеря"
        filtered_data = data[data.iloc[:, 1] == desired_value]
        unique_values_count = filtered_data[day_order].value_counts().reset_index()
        unique_values_count = pd.DataFrame(unique_values_count)
        unique_values_count4 = unique_values_count.rename(columns={day_order: 'Вечеря категорії', 'count': 'Вечеря кількість'})
        st.write(" ")
        st.write("##### Вечеря за категоріями: ")
        st.dataframe(unique_values_count4, width=800)

        
        # st.write(" ")
        # st.write(" ")
        # st.subheader(f"Формування замовлення на {day_order}: ")
        # order_text = "Замовлення на 02.11:\n Сніданок 31 (2 БЛ БГЛ)\n Обід 47 (з них 3 БЛ, БГЛ; 2 ВГ;  7 без супу) + 11 дорослих=58\n Снек 39 (4 БЛ, БГЛ,1ВЕГ) \n Вечеря 13 (1 БЛ, БГЛ,3 ВЕГ)"
        # text_to_copy = st.text_area("Текст для копіювання", order_text)
        

        # if st.button("Скопіювати текст"):
        #     st.write("Текст був скопійований", text_to_copy)
            
        
    else: 
        st.write(" ")
        st.write("На жаль, дані ***не можуть опрацюватися***, перевірте чи вказані дані записано правильно.")

else:
    st.write("Завантажте файл, щоб продовжити.")
 # Замінюємо всі значення NaN на порожні рядки
    
    


