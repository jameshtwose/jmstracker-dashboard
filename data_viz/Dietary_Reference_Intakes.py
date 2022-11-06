#%%[markdown]
# ## Dietary Reference Intakes based on the following calculator:
# https://www.nal.usda.gov/human-nutrition-and-food-safety/dri-calculator/

#%%
import pandas as pd
# %%
dri_based_on_df = pd.DataFrame({"Sex": "Male",
"Age": 28,
"Height (cm)": 182,
"Weight (kg)": 80,
"Activity level": "Low Active"
}, index=[0])
dri_based_on_df
# %%
overview_df = pd.DataFrame({
    "Body Mass Index (BMI)": 24.2,
    "Estimated Daily Caloric Needs (kcal/day)": 2898 
}, index=[0])
overview_df

# %%
macronutrient_df = pd.DataFrame({'Macronutrient': {0: 'Carbohydrate',
  1: 'Total Fiber',
  2: 'Protein',
  3: 'Fat',
  4: 'Saturated fatty acids',
  5: 'Trans fatty acids',
  6: 'α-Linolenic Acid',
  7: 'Linoleic Acid',
  8: 'Dietary Cholesterol',
  9: 'Total Water'},
 'Recommended Intake Per Day': {0: '326 - 471 grams',
  1: '38 grams',
  2: '64 grams',
  3: '64 - 113 grams',
  4: 'As low as possible while consuming a nutritionally adequate diet.',
  5: 'As low as possible while consuming a nutritionally adequate diet.',
  6: '1.6 grams',
  7: '17 grams',
  8: 'As low as possible while consuming a nutritionally adequate diet.',
  9: '3.7 liters (about 16 cups)'}})
macronutrient_df
# %%
vitamin_df = pd.DataFrame({'Vitamin': {0: 'Vitamin A',
  1: 'Vitamin C',
  2: 'Vitamin D',
  3: 'Vitamin B6',
  4: 'Vitamin E',
  5: 'Vitamin K',
  6: 'Thiamin',
  7: 'Vitamin B12',
  8: 'Riboflavin',
  9: 'Folate',
  10: 'Niacin',
  11: 'Choline',
  12: 'Pantothenic Acid',
  13: 'Biotin',
  14: 'Carotenoids'},
 'Tolerable UL Intake Per Day': {0: '3,000 mcg',
  1: '2,000 mg',
  2: '100 mcg',
  3: '100 mg',
  4: '1,000 mg',
  5: 'ND',
  6: 'ND',
  7: 'ND',
  8: 'ND',
  9: '1,000 mcg',
  10: '35 mg',
  11: '3.5 g',
  12: 'ND',
  13: 'ND',
  14: 'ND'}})
vitamin_df
# %%
mineral_df = pd.DataFrame(
    {'Mineral': {0: 'Calcium',
  1: 'Chloride',
  2: 'Chromium',
  3: 'Copper',
  4: 'Fluoride',
  5: 'Iodine',
  6: 'Iron',
  7: 'Magnesium',
  8: 'Manganese',
  9: 'Molybdenum',
  10: 'Phosphorus',
  11: 'Potassium',
  12: 'Selenium',
  13: 'Sodium',
  14: 'Zinc'},
 'Recommended Intake Per Day': {0: '1,000 mg',
  1: '2.3 g',
  2: '35 mcg',
  3: '900 mcg',
  4: '4 mg',
  5: '150 mcg',
  6: '8 mg',
  7: '400 mg',
  8: '2.3 mg',
  9: '45 mcg',
  10: '0.7 g',
  11: '3,400 mg',
  12: '55 mcg',
  13: '1,500 mg',
  14: '11 mg'},
 'Tolerable UL Intake Per Day': {0: '2,500 mg',
  1: '3.6 g',
  2: 'ND',
  3: '10,000 mcg',
  4: '10 mg',
  5: '1,100 mcg',
  6: '45 mg',
  7: '350 mg',
  8: '11 mg',
  9: '2,000 mcg',
  10: '4 g',
  11: 'ND',
  12: '400 mcg',
  13: 'ND',
  14: '40 mg'}}
)
mineral_df
