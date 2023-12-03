import streamlit as st
import pandas as pd
#from streamlit_extras.keyboard_text import key

# What is the need to find the size of household and area when calculating footprint
# Possible addition: A table where you add appliances and their consumption
# Possible addition: Waste calculation: each material and its weight

def electricity_consumption(electricity_consumption_value):
    # Carbon fotprint = electricity consumption * emission factor
    # Max value = 1200, average = 885 / month
    # emission factor for natural gas: 0.41 kgCO2e/kWh
    carbon_footprint = electricity_consumption_value * 0.41
    return carbon_footprint

def waste_footprint(df):
    paper = df.iloc[0][1] * 6
    glass = df.iloc[1][1] * 2
    metal = df.iloc[2][1] * 10
    organic = df.iloc[3][1] * 1.2
    e_waste = df.iloc[4][1] * 7
    plastic = df.iloc[5][1] * 6
    total = paper + glass + metal + organic + e_waste + plastic
    return round(total, 2)

def fuel_footprint(df):
    gasoline = df.iloc[0][1] * 2.3
    diesel = df.iloc[1][1] * 2.7
    natural_gas = df.iloc[2][1] * 2.2
    lpg = df.iloc[3][1] * 1.75
    electric = df.iloc[4][1] * 0.4
    total = gasoline + diesel + natural_gas + lpg + electric
    return round(total, 2)


st.header("Carbon Footprint Calculator", divider='green')
st.markdown("##### Please fill in the values for the inputs below to calculate your footprint")

st.header("Electrical Footprint :zap:")

url = "https://ib.bioninja.com.au/_Media/carbon-footprint_med.jpeg"
st.image(url, use_column_width="always")

electricity_consumption_value = st.slider("Electricity consumption (kWh): ", max_value=1200, min_value=200, step=50)
household_size = st.slider("Size of household: ", min_value=1, max_value=15)
carbon_footprint = electricity_consumption(electricity_consumption_value)
st.markdown("#### Your electrical footprint: " + ":red[" + str(round(carbon_footprint/household_size, 2)) + "] kgCO2e")
st.header("", divider='green')

st.header("Waste Footprint :recycle:")

url = "https://media.istockphoto.com/id/1205445735/vector/recycling-of-garbage-sorting-waste-to-different-containers-ecology-and-recycling-concept.jpg?s=612x612&w=0&k=20&c=-LBpZiUfmq8aMbIJHDwGF_VwZzgaMJXLvH_bYJEc550="
st.image(url, use_column_width="always")


df = pd.DataFrame(
    [
       {"Material": "Paper", "Weight (kg)": 5},
       {"Material": "Glass", "Weight (kg)": 5},
       {"Material": "Metal", "Weight (kg)": 3},
       {"Material": "Organic", "Weight (kg)": 3},
       {"Material": "E-Waste", "Weight (kg)": 3},
       {"Material": "Plastic", "Weight (kg)": 3},
   ]
)
edited_df = st.data_editor(df, width=1000, hide_index=True, disabled=["Material"])
st.markdown("#### Your waste footprint: " + ":red[" + str(waste_footprint(edited_df)) + "] kgCO2e")

st.header("", divider='green')

st.header("Fuel Footprint :fuelpump:")

url = "https://cdn.thezebra.com/zfront/media/production/images/8xzyovqA.width-800.jpg"
st.image(url, use_column_width="always")

df2 = pd.DataFrame(
    [
       {"Fuel": "Gasoline", "Volume (Litre)": 0},
       {"Fuel": "Diesel", "Volume (Litre)": 0},
       {"Fuel": "Natural Gas", "Volume (Litre)": 0},
       {"Fuel": "Liquefied Petroleum Gas", "Volume (Litre)": 0},
       {"Fuel": "Electric", "Volume (Litre)": 0}
   ]
)
edited_df2 = st.data_editor(df2, width=1000, hide_index=True, disabled=["Material"])
st.markdown("#### Your fuel footprint: " + ":red[" + str(fuel_footprint(edited_df2)) + "] kgCO2e")

total = str(waste_footprint(edited_df)) + (round(carbon_footprint/household_size, 2)) + (fuel_footprint(edited_df2)))

st.header("", divider='green')
st.header("_Your total footprint is_ " + ":green[" + total + "] kgCO2e", divider='green')
