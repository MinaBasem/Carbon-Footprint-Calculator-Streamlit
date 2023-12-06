import streamlit as st
import pandas as pd

tab1, tab2 = st.tabs(["Original", 'Modified'])

def electrical_footprint(df):
    df["Calculated kWh"] = df["Amount"] * df["Hours Running"]
    #                       AMOUNT        * HOURS
    refrigerator =          df.iloc[0][1] * df.iloc[0][2] * 1.5/24
    freezer =               df.iloc[1][1] * df.iloc[1][2] * 2/24
    dishwasher =            df.iloc[2][1] * df.iloc[2][2] * 1.5/24
    washing_machine =       df.iloc[3][1] * df.iloc[3][2] * 1.5
    microwave =             df.iloc[4][1] * df.iloc[4][2] * 1.2
    air_conditioner =       df.iloc[5][1] * df.iloc[5][2] * 1.1
    fan =                   df.iloc[6][1] * df.iloc[6][2] * 0.7
    television =            df.iloc[7][1] * df.iloc[7][2] * 0.15
    led_lights =            df.iloc[8][1] * df.iloc[8][2] * 0.008
    total = refrigerator + freezer + dishwasher + washing_machine + microwave + air_conditioner + fan + television + led_lights
    carbon_footprint = total/1000 * 400 # Average carbon intensity is 400 kgCO2e/kWh
    return round(carbon_footprint, 2)

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


with tab1:

    st.header("Carbon Footprint Calculator", divider='green')
    st.markdown("##### Please fill in the values for the inputs below to calculate your footprint")

    st.header("Electrical Footprint :zap:")

    url = "https://ib.bioninja.com.au/_Media/carbon-footprint_med.jpeg"
    st.image(url, use_column_width="always")

    electricity_consumption_value = st.slider("Electricity consumption (kWh): ", max_value=1200, min_value=200, step=50)
    household_size = st.slider("Size of household: ", min_value=1, max_value=15)
    carbon_footprint = electricity_consumption(electricity_consumption_value)
    st.markdown("#### Your electrical footprint: " + ":red[" + str(round(carbon_footprint/household_size, 2)) + "] kgCO2e")
    st.divider()

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

    st.divider()

    fuel_df_tab1 = pd.DataFrame(
        [
        {"Fuel": "Gasoline", "Volume (Litre)": 0},
        {"Fuel": "Diesel", "Volume (Litre)": 0},
        {"Fuel": "Natural Gas", "Volume (Litre)": 0},
        {"Fuel": "Liquefied Petroleum Gas", "Volume (Litre)": 0},
        {"Fuel": "Electric", "Volume (Litre)": 0}
    ]
    )
    fuel_df_tab1 = st.data_editor(fuel_df_tab1, width=1000, hide_index=True, disabled=["Fuel"])
    st.markdown("#### Your waste footprint: " + ":red[" + str(fuel_footprint(fuel_df_tab1)) + "] kgCO2e")

    total = str(round((waste_footprint(edited_df)) + (carbon_footprint/household_size) + (fuel_footprint(fuel_df_tab1)), 2))

    st.header("", divider='green')
    st.header("_Your total footprint is_ " + ":green[" + total + "] kgCO2e", divider='green')

# ---------------------------------------------------------------------------

with tab2:
    def electricity_consumption(electricity_consumption_value):
        # Carbon fotprint = electricity consumption * emission factor
        # Max value = 1200, average = 885 / month
        # emission factor for natural gas: 0.41 kgCO2e/kWh
        carbon_footprint = electricity_consumption_value * 0.41
        return carbon_footprint

    st.header("Carbon Footprint Calculator", divider='green')
    st.markdown("##### Please fill in the values for the inputs below to calculate your footprint")

    st.header("Electrical Footprint :zap:")

    url = "https://promova.com/content/kitchen_appliances_names_c099006f30.png"
    st.image(url, use_column_width="always")

    appliances_data_df_tab2 = pd.DataFrame([
        {"Appliance Name": "Refrigerator", "Amount": 1, "Hours Running": 0},
        {"Appliance Name": "Freezer", "Amount": 1, "Hours Running": 0},
        {"Appliance Name": "Dishwasher", "Amount": 1, "Hours Running": 0},
        {"Appliance Name": "Washing Machine", "Amount": 1, "Hours Running": 0},
        {"Appliance Name": "Microwave", "Amount": 1, "Hours Running": 0},
        {"Appliance Name": "Air Conditioner", "Amount": 1, "Hours Running": 0},
        {"Appliance Name": "Fan", "Amount": 1, "Hours Running": 0},
        {"Appliance Name": "Television", "Amount": 1, "Hours Running": 0},
        {"Appliance Name": "LED Lights", "Amount": 1, "Hours Running": 0},
        # Add other appliances here...
    ])

    # update values of Calculated kWh column to multiply Amount column by Hours Running column

    appliances_data_df_tab2 = st.data_editor(appliances_data_df_tab2, width=1000, hide_index=True, disabled=["Appliance Name"])
    electrical_footprint(appliances_data_df_tab2)

    st.markdown("#### Your electrical footprint: " + ":red[~" + str(electrical_footprint(appliances_data_df_tab2)) + "] kgCO2e")
    st.divider()

    st.header("Waste Footprint :recycle:")

    url = "https://media.istockphoto.com/id/1205445735/vector/recycling-of-garbage-sorting-waste-to-different-containers-ecology-and-recycling-concept.jpg?s=612x612&w=0&k=20&c=-LBpZiUfmq8aMbIJHDwGF_VwZzgaMJXLvH_bYJEc550="
    st.image(url, use_column_width="always")


    waste_df_tab2 = pd.DataFrame(
        [
        {"Material": "Paper", "Weight (kg)": 5},
        {"Material": "Glass", "Weight (kg)": 5},
        {"Material": "Metal", "Weight (kg)": 3},
        {"Material": "Organic", "Weight (kg)": 3},
        {"Material": "E-Waste", "Weight (kg)": 3},
        {"Material": "Plastic", "Weight (kg)": 3},
    ]
    )
    waste_df_tab2 = st.data_editor(waste_df_tab2, width=1000, hide_index=True, disabled=["Material"], key="100")
    st.markdown("#### Your waste footprint: " + ":red[~" + str(waste_footprint(waste_df_tab2)) + "] kgCO2e")

    st.divider()

    fuel_df_tab2 = pd.DataFrame(
        [
        {"Fuel": "Gasoline", "Volume (Litre)": 0},
        {"Fuel": "Diesel", "Volume (Litre)": 0},
        {"Fuel": "Natural Gas", "Volume (Litre)": 0},
        {"Fuel": "Liquefied Petroleum Gas", "Volume (Litre)": 0},
        {"Fuel": "Electric", "Volume (Litre)": 0}
    ]
    )
    fuel_df_tab2 = st.data_editor(fuel_df_tab2, width=1000, hide_index=True, disabled=["Fuel"], key="200")
    st.markdown("#### Your waste footprint: " + ":red[~" + str(fuel_footprint(fuel_df_tab2)) + "] kgCO2e")

    total = str(round((waste_footprint(edited_df)) + electrical_footprint(appliances_data_df_tab2) + (fuel_footprint(fuel_df_tab2)), 2))

    st.header("", divider='green')
    st.header("_Your total footprint is_ " + ":green[~" + total + "] kgCO2e", divider='green')



