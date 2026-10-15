import streamlit as st

st.set_page_config(
    page_title="Where Is Room?",
    page_icon="🏠"
)

st.title("🏠 Where Is Room?")
st.subheader("Students ke liye Room Finder")

st.write("Apne budget mein room, PG ya hostel khojiye!")

rooms = [
    {
        "city": "Purnia",
        "name": "Student Room",
        "type": "Room",
        "rent": 2500,
        "location": "Line Bazar",
        "facilities": "Bed, Fan, Wi-Fi"
    },
    {
        "city": "Purnia",
        "name": "Student PG",
        "type": "PG",
        "rent": 3500,
        "location": "Madhubani",
        "facilities": "Food, Water, Wi-Fi"
    },
    {
        "city": "Patna",
        "name": "Student Hostel",
        "type": "Hostel",
        "rent": 4000,
        "location": "Boring Road",
        "facilities": "Bed, Food, Wi-Fi"
    }
]

city = st.text_input("Apna city likhein")

kind = st.selectbox(
    "Room ka type chunein",
    ["Sabhi", "Room", "PG", "Hostel"]
)

budget = st.slider(
    "Maximum rent per month (₹)",
    1000, 10000, 5000, step=500
)

if st.button("Search Room"):
    found = [
        r for r in rooms
        if (not city or city.lower() in r["city"].lower())
        and (kind == "Sabhi" or kind == r["type"])
        and r["rent"] <= budget
    ]

    if found:
        st.success(f"{len(found)} listings mili!")

        for r in found:
            with st.container(border=True):
                st.subheader("🏠 " + r["name"])
                st.write("City:", r["city"])
                st.write("Location:", r["location"])
                st.write("Type:", r["type"])
                st.write(f"Rent: ₹{r['rent']}/month")
                st.write("Facilities:", r["facilities"])
    else:
        st.warning("Koi room nahi mila. Budget ya city badlein.")

st.caption("Where Is Room? — Demo Version")
