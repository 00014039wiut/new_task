# ai_models.py
from baton.ai import AIModels

models = {
    'IMAGES_MODEL': AIModels.BATON_DALL_E_3,
    'SUMMARIZATIONS_MODEL': AIModels.BATON_GPT_4O,
    'TRANSLATIONS_MODEL': AIModels.BATON_GPT_4O,
    'CORRECTIONS_MODEL': AIModels.BATON_GPT_3_5_TURBO,
}
