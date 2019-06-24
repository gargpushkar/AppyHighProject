import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, os.pardir)))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from Food.models import FoodStore


import csv

csv.field_size_limit(sys.maxsize)
csv.field_size_limit(sys.maxsize)

print("Reading tsv file....")

food_list=[]
with open('en.openfoodfacts.org.products.tsv', encoding='utf-8' ) as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  for row in reader:
    food_list.append(row)

print("Inserting Rows in DB....")

column_name = food_list[0]

count=step=25000

for i in range(2,len(food_list)):
    if i == count:
        count += step
        print(i)
    obj = {}
    for j in range(0,163):
        if j < len(food_list[i]):
            obj[column_name[j]] = food_list[i][j]
        else:
            obj[column_name[j]] = ""

    FoodStore.objects.create(
        code  =  obj["code"],
        url  =  obj["url"],
        creator  =  obj["creator"],
        created_t  =  obj["created_t"],
        created_datetime  =  obj["created_datetime"],
        last_modified_t  =  obj["last_modified_t"],
        last_modified_datetime  =  obj["last_modified_datetime"],
        product_name  =  obj["product_name"],
        generic_name  =  obj["generic_name"],
        quantity  =  obj["quantity"],
        packaging  =  obj["packaging"],
        packaging_tags  =  obj["packaging_tags"],
        brands  =  obj["brands"],
        brands_tags  =  obj["brands_tags"],
        categories  =  obj["categories"],
        categories_tags  =  obj["categories_tags"],
        categories_en  =  obj["categories_en"],
        origins  =  obj["origins"],
        origins_tags  =  obj["origins_tags"],
        manufacturing_places  =  obj["manufacturing_places"],
        manufacturing_places_tags  =  obj["manufacturing_places_tags"],
        labels  =  obj["labels"],
        labels_tags  =  obj["labels_tags"],
        labels_en  =  obj["labels_en"],
        emb_codes  =  obj["emb_codes"],
        emb_codes_tags  =  obj["emb_codes_tags"],
        first_packaging_code_geo  =  obj["first_packaging_code_geo"],
        cities  =  obj["cities"],
        cities_tags  =  obj["cities_tags"],
        purchase_places  =  obj["purchase_places"],
        stores  =  obj["stores"],
        countries  =  obj["countries"],
        countries_tags  =  obj["countries_tags"],
        countries_en  =  obj["countries_en"],
        ingredients_text  =  obj["ingredients_text"],
        allergens  =  obj["allergens"],
        allergens_en  =  obj["allergens_en"],
        traces  =  obj["traces"],
        traces_tags  =  obj["traces_tags"],
        traces_en  =  obj["traces_en"],
        serving_size  =  obj["serving_size"],
        no_nutriments  =  obj["no_nutriments"],
        additives_n  =  obj["additives_n"],
        additives  =  obj["additives"],
        additives_tags  =  obj["additives_tags"],
        additives_en  =  obj["additives_en"],
        ingredients_from_palm_oil_n  =  obj["ingredients_from_palm_oil_n"],
        ingredients_from_palm_oil  =  obj["ingredients_from_palm_oil"],
        ingredients_from_palm_oil_tags  =  obj["ingredients_from_palm_oil_tags"],
        ingredients_that_may_be_from_palm_oil_n  =  obj["ingredients_that_may_be_from_palm_oil_n"],
        ingredients_that_may_be_from_palm_oil  =  obj["ingredients_that_may_be_from_palm_oil"],
        ingredients_that_may_be_from_palm_oil_tags  =  obj["ingredients_that_may_be_from_palm_oil_tags"],
        nutrition_grade_uk  =  obj["nutrition_grade_uk"],
        nutrition_grade_fr  =  obj["nutrition_grade_fr"],
        pnns_groups_1  =  obj["pnns_groups_1"],
        pnns_groups_2  =  obj["pnns_groups_2"],
        states  =  obj["states"],
        states_tags  =  obj["states_tags"],
        states_en  =  obj["states_en"],
        main_category  =  obj["main_category"],
        main_category_en  =  obj["main_category_en"],
        image_url  =  obj["image_url"],
        image_small_url  =  obj["image_small_url"],
        energy_100g  =  obj["energy_100g"],
        energyfromfat_100g  =  obj["energy-from-fat_100g"],
        fat_100g  =  obj["fat_100g"],
        saturatedfat_100g  =  obj["saturated-fat_100g"],
        butyricacid_100g  =  obj["-butyric-acid_100g"],
        caproicacid_100g  =  obj["-caproic-acid_100g"],
        caprylicacid_100g  =  obj["-caprylic-acid_100g"],
        capricacid_100g  =  obj["-capric-acid_100g"],
        lauricacid_100g  =  obj["-lauric-acid_100g"],
        myristicacid_100g  =  obj["-myristic-acid_100g"],
        palmiticacid_100g  =  obj["-palmitic-acid_100g"],
        stearicacid_100g  =  obj["-stearic-acid_100g"],
        arachidicacid_100g  =  obj["-arachidic-acid_100g"],
        behenicacid_100g  =  obj["-behenic-acid_100g"],
        lignocericacid_100g  =  obj["-lignoceric-acid_100g"],
        ceroticacid_100g  =  obj["-cerotic-acid_100g"],
        montanicacid_100g  =  obj["-montanic-acid_100g"],
        melissicacid_100g  =  obj["-melissic-acid_100g"],
        monounsaturatedfat_100g  =  obj["monounsaturated-fat_100g"],
        polyunsaturatedfat_100g  =  obj["polyunsaturated-fat_100g"],
        omega3fat_100g  =  obj["omega-3-fat_100g"],
        alphalinolenicacid_100g  =  obj["-alpha-linolenic-acid_100g"],
        eicosapentaenoicacid_100g  =  obj["-eicosapentaenoic-acid_100g"],
        docosahexaenoicacid_100g  =  obj["-docosahexaenoic-acid_100g"],
        omega6fat_100g  =  obj["omega-6-fat_100g"],
        linoleicacid_100g  =  obj["-linoleic-acid_100g"],
        arachidonicacid_100g  =  obj["-arachidonic-acid_100g"],
        gammalinolenicacid_100g  =  obj["-gamma-linolenic-acid_100g"],
        dihomogammalinolenicacid_100g  =  obj["-dihomo-gamma-linolenic-acid_100g"],
        omega9fat_100g  =  obj["omega-9-fat_100g"],
        oleicacid_100g  =  obj["-oleic-acid_100g"],
        elaidicacid_100g  =  obj["-elaidic-acid_100g"],
        gondoicacid_100g  =  obj["-gondoic-acid_100g"],
        meadacid_100g  =  obj["-mead-acid_100g"],
        erucicacid_100g  =  obj["-erucic-acid_100g"],
        nervonicacid_100g  =  obj["-nervonic-acid_100g"],
        transfat_100g  =  obj["trans-fat_100g"],
        cholesterol_100g  =  obj["cholesterol_100g"],
        carbohydrates_100g  =  obj["carbohydrates_100g"],
        sugars_100g  =  obj["sugars_100g"],
        sucrose_100g  =  obj["-sucrose_100g"],
        glucose_100g  =  obj["-glucose_100g"],
        fructose_100g  =  obj["-fructose_100g"],
        lactose_100g  =  obj["-lactose_100g"],
        maltose_100g  =  obj["-maltose_100g"],
        maltodextrins_100g  =  obj["-maltodextrins_100g"],
        starch_100g  =  obj["starch_100g"],
        polyols_100g  =  obj["polyols_100g"],
        fiber_100g  =  obj["fiber_100g"],
        proteins_100g  =  obj["proteins_100g"],
        casein_100g  =  obj["casein_100g"],
        serumproteins_100g  =  obj["serum-proteins_100g"],
        nucleotides_100g  =  obj["nucleotides_100g"],
        salt_100g  =  obj["salt_100g"],
        sodium_100g  =  obj["sodium_100g"],
        alcohol_100g  =  obj["alcohol_100g"],
        vitamina_100g  =  obj["vitamin-a_100g"],
        betacarotene_100g  =  obj["beta-carotene_100g"],
        vitamind_100g  =  obj["vitamin-d_100g"],
        vitamine_100g  =  obj["vitamin-e_100g"],
        vitamink_100g  =  obj["vitamin-k_100g"],
        vitaminc_100g  =  obj["vitamin-c_100g"],
        vitaminb1_100g  =  obj["vitamin-b1_100g"],
        vitaminb2_100g  =  obj["vitamin-b2_100g"],
        vitaminpp_100g  =  obj["vitamin-pp_100g"],
        vitaminb6_100g  =  obj["vitamin-b6_100g"],
        vitaminb9_100g  =  obj["vitamin-b9_100g"],
        folates_100g  =  obj["folates_100g"],
        vitaminb12_100g  =  obj["vitamin-b12_100g"],
        biotin_100g  =  obj["biotin_100g"],
        pantothenicacid_100g  =  obj["pantothenic-acid_100g"],
        silica_100g  =  obj["silica_100g"],
        bicarbonate_100g  =  obj["bicarbonate_100g"],
        potassium_100g  =  obj["potassium_100g"],
        chloride_100g  =  obj["chloride_100g"],
        calcium_100g  =  obj["calcium_100g"],
        phosphorus_100g  =  obj["phosphorus_100g"],
        iron_100g  =  obj["iron_100g"],
        magnesium_100g  =  obj["magnesium_100g"],
        zinc_100g  =  obj["zinc_100g"],
        copper_100g  =  obj["copper_100g"],
        manganese_100g  =  obj["manganese_100g"],
        fluoride_100g  =  obj["fluoride_100g"],
        selenium_100g  =  obj["selenium_100g"],
        chromium_100g  =  obj["chromium_100g"],
        molybdenum_100g  =  obj["molybdenum_100g"],
        iodine_100g  =  obj["iodine_100g"],
        caffeine_100g  =  obj["caffeine_100g"],
        taurine_100g  =  obj["taurine_100g"],
        ph_100g  =  obj["ph_100g"],
        fruitsvegetablesnuts_100g  =  obj["fruits-vegetables-nuts_100g"],
        fruitsvegetablesnutsestimate_100g  =  obj["fruits-vegetables-nuts-estimate_100g"],
        collagenmeatproteinratio_100g  =  obj["collagen-meat-protein-ratio_100g"],
        cocoa_100g  =  obj["cocoa_100g"],
        chlorophyl_100g  =  obj["chlorophyl_100g"],
        carbonfootprint_100g  =  obj["carbon-footprint_100g"],
        nutritionscorefr_100g  =  obj["nutrition-score-fr_100g"],
        nutritionscoreuk_100g  =  obj["nutrition-score-uk_100g"],
        glycemicindex_100g  =  obj["glycemic-index_100g"],
        waterhardness_100g  =  obj["water-hardness_100g"]
    )

print("Success")