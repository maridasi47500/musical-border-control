
mkdir templates 
python3 scaffold.py user username email password country_id:references phone
python3 scaffold.py custom_officer name country_id:references
python3 scaffold.py country name
python3 scaffold.py customofficierhasuser custom_officer_id:references user_id:references
python3 scaffold.py hit artist title
python3 scaffold.py musicalinstrument name
python3 scaffold.py userhasmusicalinstrument musicalinstrument_id:references user_id
python3 scaffold.py userhashit hit_id user_id
python3 scaffold.py userhasrythme hit_id rythme user_id:references
python3 scaffold.py userhassignaturemusicale motif_musical hit_id style_id
python3 scaffold.py style name
python3 scaffold.py performance user_id style_id:references artist composer title
