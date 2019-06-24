from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class FoodStore(models.Model):
    """Model definition for FoodStore."""
    code                                       =  models.CharField( null=True,max_length=40)  
    url                                        =  models.URLField( null=True, max_length=200)
    creator                                    =  models.CharField( null=True,max_length=40)
    created_t                                  =  models.CharField( null=True,max_length=100)
    created_datetime                           =  models.CharField( null=True,max_length=100)
    last_modified_t                            =  models.CharField( null=True,max_length=100)
    last_modified_datetime                     =  models.CharField( null=True,max_length=100) 
    product_name                               =  models.CharField( max_length=50, null = False) 
    generic_name                               =  models.CharField( null=True,max_length=100) 
    quantity                                   =  models.CharField( null=True,max_length=100) 
    packaging                                  =  models.CharField( null=True,max_length=100) 
    packaging_tags                             =  models.CharField( null=True,max_length=200) 
    brands                                     =  models.CharField( null=True,max_length=100) 
    brands_tags                                =  models.CharField( null=True,max_length=200) 
    categories                                 =  models.CharField( null=True,max_length=100) 
    categories_tags                            =  models.CharField( null=True,max_length=200) 
    categories_en                              =  models.CharField( null=True,max_length=200) 
    origins                                    =  models.CharField( null=True,max_length=100) 
    origins_tags                               =  models.CharField( null=True,max_length=200) 
    manufacturing_places                       =  models.CharField( null=True,max_length=100) 
    manufacturing_places_tags                  =  models.CharField( null=True,max_length=200) 
    labels                                     =  models.CharField( null=True,max_length=100) 
    labels_tags                                =  models.CharField( null=True,max_length=200) 
    labels_en                                  =  models.CharField( null=True,max_length=100) 
    emb_codes                                  =  models.CharField( null=True,max_length=200) 
    emb_codes_tags                             =  models.CharField( null=True,max_length=100) 
    first_packaging_code_geo                   =  models.CharField( null=True,max_length=100) 
    cities                                     =  models.CharField( null=True,max_length=100) 
    cities_tags                                =  models.CharField( null=True,max_length=200) 
    purchase_places                            =  models.CharField( null=True,max_length=100) 
    stores                                     =  models.CharField( null=True,max_length=100) 
    countries                                  =  models.CharField( null=True,max_length=100)
    countries_tags                             =  models.CharField( null=True,max_length=100)
    countries_en                               =  models.CharField( null=True,max_length=100)
    ingredients_text                           =  models.CharField( null=True,max_length=1000)  
    allergens                                  =  models.CharField( null=True,max_length=100)
    allergens_en                               =  models.CharField( null=True,max_length=100)
    traces                                     =  models.CharField( null=True,max_length=100)
    traces_tags                                =  models.CharField( null=True,max_length=100)
    traces_en                                  =  models.CharField( null=True,max_length=100)
    serving_size                               =  models.CharField( null=True,max_length=100)
    no_nutriments                              =  models.CharField( null=True,max_length=100)
    additives_n                                =  models.CharField( null=True,max_length=10)
    additives                                  =  models.CharField( null=True,max_length=1200)
    additives_tags                             =  models.CharField( null=True,max_length=120) 
    additives_en                               =  models.CharField( null=True,max_length=100) 
    ingredients_from_palm_oil_n                =  models.CharField( null=True,max_length=100)
    ingredients_from_palm_oil                  =  models.CharField( null=True,max_length=100) 
    ingredients_from_palm_oil_tags             =  models.CharField( null=True,max_length=100) 
    ingredients_that_may_be_from_palm_oil_n    =  models.CharField( null=True,max_length=10)
    ingredients_that_may_be_from_palm_oil      =  models.CharField( null=True,max_length=100)  
    ingredients_that_may_be_from_palm_oil_tags =  models.CharField( null=True,max_length=100)  
    nutrition_grade_uk                         =  models.CharField( null=True,max_length=100)  
    nutrition_grade_fr                         =  models.CharField( null=True,max_length=100)  
    pnns_groups_1                              =  models.CharField( null=True,max_length=100)  
    pnns_groups_2                              =  models.CharField( null=True,max_length=100)  
    states                                     =  models.CharField( null=True,max_length=500)
    states_tags                                =  models.CharField( null=True,max_length=500)
    states_en                                  =  models.CharField( null=True,max_length=500)
    main_category                              =  models.CharField( null=True,max_length=100)  
    main_category_en                           =  models.CharField( null=True,max_length=100)  
    image_url                                  =  models.CharField( null=True,max_length=100)  
    image_small_url                            =  models.CharField( null=True,max_length=100)  
    energy_100g                                =  models.CharField( null=True,max_length=100) 
    energyfromfat_100g                         =  models.CharField( null=True,max_length=100) 
    fat_100g                                   =  models.CharField( null=True,max_length=100)
    saturatedfat_100g                          =  models.CharField( null=True,max_length=100)
    butyricacid_100g                           =  models.CharField( null=True,max_length=100) 
    caproicacid_100g                           =  models.CharField( null=True,max_length=100) 
    caprylicacid_100g                          =  models.CharField( null=True,max_length=100) 
    capricacid_100g                            =  models.CharField( null=True,max_length=100) 
    lauricacid_100g                            =  models.CharField( null=True,max_length=100) 
    myristicacid_100g                          =  models.CharField( null=True,max_length=100) 
    palmiticacid_100g                          =  models.CharField( null=True,max_length=100) 
    stearicacid_100g                           =  models.CharField( null=True,max_length=100) 
    arachidicacid_100g                         =  models.CharField( null=True,max_length=100) 
    behenicacid_100g                           =  models.CharField( null=True,max_length=100) 
    lignocericacid_100g                        =  models.CharField( null=True,max_length=100) 
    ceroticacid_100g                           =  models.CharField( null=True,max_length=100) 
    montanicacid_100g                          =  models.CharField( null=True,max_length=100) 
    melissicacid_100g                          =  models.CharField( null=True,max_length=100) 
    monounsaturatedfat_100g                    =  models.CharField( null=True,max_length=100) 
    polyunsaturatedfat_100g                    =  models.CharField( null=True,max_length=100) 
    omega3fat_100g                             =  models.CharField( null=True,max_length=100) 
    alphalinolenicacid_100g                    =  models.CharField( null=True,max_length=100) 
    eicosapentaenoicacid_100g                  =  models.CharField( null=True,max_length=100) 
    docosahexaenoicacid_100g                   =  models.CharField( null=True,max_length=100) 
    omega6fat_100g                             =  models.CharField( null=True,max_length=100) 
    linoleicacid_100g                          =  models.CharField( null=True,max_length=100) 
    arachidonicacid_100g                       =  models.CharField( null=True,max_length=100) 
    gammalinolenicacid_100g                    =  models.CharField( null=True,max_length=100) 
    dihomogammalinolenicacid_100g              =  models.CharField( null=True,max_length=100) 
    omega9fat_100g                             =  models.CharField( null=True,max_length=100) 
    oleicacid_100g                             =  models.CharField( null=True,max_length=100) 
    elaidicacid_100g                           =  models.CharField( null=True,max_length=100) 
    gondoicacid_100g                           =  models.CharField( null=True,max_length=100) 
    meadacid_100g                              =  models.CharField( null=True,max_length=100) 
    erucicacid_100g                            =  models.CharField( null=True,max_length=100) 
    nervonicacid_100g                          =  models.CharField( null=True,max_length=100) 
    transfat_100g                              =  models.CharField( null=True,max_length=100)
    cholesterol_100g                           =  models.CharField( null=True,max_length=100)
    carbohydrates_100g                         =  models.CharField( null=True,max_length=100)
    sugars_100g                                =  models.CharField( null=True,max_length=100)
    sucrose_100g                               =  models.CharField( null=True,max_length=100)  
    glucose_100g                               =  models.CharField( null=True,max_length=100)  
    fructose_100g                              =  models.CharField( null=True,max_length=100)  
    lactose_100g                               =  models.CharField( null=True,max_length=100)  
    maltose_100g                               =  models.CharField( null=True,max_length=100)  
    maltodextrins_100g                         =  models.CharField( null=True,max_length=100)  
    starch_100g                                =  models.CharField( null=True,max_length=100)  
    polyols_100g                               =  models.CharField( null=True,max_length=100)  
    fiber_100g                                 =  models.CharField( null=True,max_length=100)
    proteins_100g                              =  models.CharField( null=True,max_length=100)
    casein_100g                                =  models.CharField( null=True,max_length=100)  
    serumproteins_100g                         =  models.CharField( null=True,max_length=100)  
    nucleotides_100g                           =  models.CharField( null=True,max_length=100)  
    salt_100g                                  =  models.CharField( null=True,max_length=100)
    sodium_100g                                =  models.CharField( null=True,max_length=100)
    alcohol_100g                               =  models.CharField( null=True,max_length=100)  
    vitamina_100g                              =  models.CharField( null=True,max_length=100)
    betacarotene_100g                          =  models.CharField( null=True,max_length=100)  
    vitamind_100g                              =  models.CharField( null=True,max_length=100)  
    vitamine_100g                              =  models.CharField( null=True,max_length=100)  
    vitamink_100g                              =  models.CharField( null=True,max_length=100)  
    vitaminc_100g                              =  models.CharField( null=True,max_length=100)
    vitaminb1_100g                             =  models.CharField( null=True,max_length=100)  
    vitaminb2_100g                             =  models.CharField( null=True,max_length=100)  
    vitaminpp_100g                             =  models.CharField( null=True,max_length=100)  
    vitaminb6_100g                             =  models.CharField( null=True,max_length=100)  
    vitaminb9_100g                             =  models.CharField( null=True,max_length=100)  
    folates_100g                               =  models.CharField( null=True,max_length=100)  
    vitaminb12_100g                            =  models.CharField( null=True,max_length=100)  
    biotin_100g                                =  models.CharField( null=True,max_length=100)  
    pantothenicacid_100g                       =  models.CharField( null=True,max_length=100)  
    silica_100g                                =  models.CharField( null=True,max_length=100)  
    bicarbonate_100g                           =  models.CharField( null=True,max_length=100)  
    potassium_100g                             =  models.CharField( null=True,max_length=100)  
    chloride_100g                              =  models.CharField( null=True,max_length=100)  
    calcium_100g                               =  models.CharField( null=True,max_length=100)
    phosphorus_100g                            =  models.CharField( null=True,max_length=100) 
    iron_100g                                  =  models.CharField( null=True,max_length=100)
    magnesium_100g                             =  models.CharField( null=True,max_length=100)  
    zinc_100g                                  =  models.CharField( null=True,max_length=100)  
    copper_100g                                =  models.CharField( null=True,max_length=100)  
    manganese_100g                             =  models.CharField( null=True,max_length=100)  
    fluoride_100g                              =  models.CharField( null=True,max_length=100)  
    selenium_100g                              =  models.CharField( null=True,max_length=100)  
    chromium_100g                              =  models.CharField( null=True,max_length=100)  
    molybdenum_100g                            =  models.CharField( null=True,max_length=100)  
    iodine_100g                                =  models.CharField( null=True,max_length=100)  
    caffeine_100g                              =  models.CharField( null=True,max_length=100)  
    taurine_100g                               =  models.CharField( null=True,max_length=100)  
    ph_100g                                    =  models.CharField( null=True,max_length=100)  
    fruitsvegetablesnuts_100g                  =  models.CharField( null=True,max_length=100)  
    fruitsvegetablesnutsestimate_100g          =  models.CharField( null=True,max_length=100)  
    collagenmeatproteinratio_100g              =  models.CharField( null=True,max_length=100)  
    cocoa_100g                                 =  models.CharField( null=True,max_length=100)  
    chlorophyl_100g                            =  models.CharField( null=True,max_length=100)  
    carbonfootprint_100g                       =  models.CharField( null=True,max_length=100)  
    nutritionscorefr_100g                      =  models.CharField( null=True,max_length=100)  
    nutritionscoreuk_100g                      =  models.CharField( null=True,max_length=100)  
    glycemicindex_100g                         =  models.CharField( null=True,max_length=100) 
    waterhardness_100g                         =  models.CharField( null=True,max_length=100) 

    class Meta:
        """Meta definition for FoodStore."""

        verbose_name = 'FoodStore'
        verbose_name_plural = 'FoodStores'

    def __str__(self):
        """Unicode representation of FoodStore."""
        if self.product_name !=  '':
           return self.product_name
        else:
            return "Food Object"
    
    def get_absolute_url(self):
        return reverse('Food:detail', kwargs={'pk': self.pk})
