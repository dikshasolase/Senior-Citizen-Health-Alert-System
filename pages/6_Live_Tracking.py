import streamlit as st
import streamlit.components.v1 as components


# Page Configuration

st.set_page_config(
    page_title="Nearby Hospitals",
    page_icon="🏥",
    layout="wide"
)


# Title

st.title("🏥 Nearby Hospitals")

st.divider()


st.write(
    "Find hospitals near your current location"
)



# Button

hospital_button = """

<button onclick="findHospitals()"
style="
background:#e63946;
color:white;
border:none;
padding:10px 20px;
border-radius:8px;
font-size:16px;
cursor:pointer;
">
🏥 Find Nearby Hospitals
</button>


<script>

function findHospitals(){


navigator.geolocation.getCurrentPosition(

function(position){


let latitude =
position.coords.latitude;


let longitude =
position.coords.longitude;



let url =
"https://www.google.com/maps/search/hospitals/@"
+
latitude
+
","
+
longitude
+
",14z";



window.open(
url,
"_blank"
);



},


function(){

alert(
"Please allow location permission"
);

}


);


}

</script>

"""


components.html(
    hospital_button,
    height=80
)



st.divider()


