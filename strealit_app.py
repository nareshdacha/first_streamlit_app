import streamlit
import requests
import pandas
streamlit.title('Naresh Testing')
streamlit.header('Laptop')
streamlit.text('Testing Messages')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#,options=['Avacado','Strawberries']
#streamlit.dataframe(my_fruit_list)
#fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_selected)
streamlit.header('Fruitvice Fruit Advice')
import requests
f_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(f_response.json())
fruitvice_norm = pandas.json_normalize(f_response.json())
streamlit.dataframe(fruitvice_norm )
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
