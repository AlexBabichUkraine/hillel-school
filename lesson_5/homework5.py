from decimal import Decimal
from pywebio.input import input as pw_input, FLOAT
from pywebio.output import put_success, put_warning

# kKal/100gr of products

OSTRICH_EGG_KKAL = 118
RABBIT_KKAL = 197
SEA_FISH_KKAL = 123
RED_PEPPER_SWEET_KKAL = 26
GREEN_GRASS_KKAL = 45
BANANAS_KKAL = 87
WAFFLES_KKAL = 425
GRAIN_BREAD_FIRST_CLASS_KKAL = 246
PISTACHIO_KKAL = 555
KEFIR_25_KKAL = 51
ONE_KKAL_PRICE = 0.32541

total_energy = 0

ostrich_egg_weight = pw_input(f"Please enter how much grams of ostrich's eggs \U0001F95A you want: \n"
                              f"Calories {OSTRICH_EGG_KKAL} Kkal/100gr.", type=FLOAT)
ostrich_egg_total_energy = round(ostrich_egg_weight * OSTRICH_EGG_KKAL / 100, 2)
total_energy += ostrich_egg_total_energy
put_success(f"You ordered {ostrich_egg_weight} grams of ostrich eggs \U0001F95A \n"
            f"Calories of portion: {ostrich_egg_total_energy} kkal \n"
            f"Total calories intakes: {total_energy} kkal")

rabbit_meat_weight = pw_input(f"Please enter how much grams of rabbit meat \U0001F407 you want: \n"
                              f"Calories {RABBIT_KKAL} Kkal/100gr.", type=FLOAT)
rabbit_meat_total_energy = round(rabbit_meat_weight * RABBIT_KKAL / 100, 2)
total_energy += rabbit_meat_total_energy
put_success(f"You ordered {rabbit_meat_weight} grams of rabbit meat \U0001F407 \n"
            f"Calories of portion: {rabbit_meat_total_energy} kkal \n"
            f"Total calories intakes: {total_energy} kkal")

sea_fish_weight = pw_input(f"Please enter how much grams of sea fish \U0001F988 you want: \n"
                           f"Calories {SEA_FISH_KKAL} Kkal/100gr.", type=FLOAT)
sea_fish_total_energy = round(sea_fish_weight * SEA_FISH_KKAL / 100, 2)
total_energy += sea_fish_total_energy
put_success(f"You ordered {sea_fish_weight} grams of sea fish \U0001F988 \n"
            f"Calories of portion: {sea_fish_total_energy} kkal \n"
            f"Total calories intakes: {total_energy} kkal")

red_pepper_weight = pw_input(f"Please enter how much grams of sweet red pepper \U0001F336 you want: \n"
                             f"Calories {RED_PEPPER_SWEET_KKAL} Kkal/100gr.", type=FLOAT)
red_pepper_total_energy = round(red_pepper_weight * RED_PEPPER_SWEET_KKAL / 100, 2)
total_energy += red_pepper_total_energy
put_success(f"You ordered {red_pepper_weight} grams of sweet red pepper \U0001F336 \n"
            f"Calories of portion: {red_pepper_total_energy} kkal \n"
            f"Total calories intakes: {total_energy} kkal")

green_grass_weight = pw_input(f"Please enter how much grams of green grass \U0001F96C you want: \n"
                              f"Calories {GREEN_GRASS_KKAL} Kkal/100gr.", type=FLOAT)
green_grass_total_energy = round(green_grass_weight * GREEN_GRASS_KKAL / 100, 2)
total_energy += green_grass_total_energy
put_success(f"You ordered {green_grass_weight} grams of green grass \U0001F96C \n"
            f"Calories of portion: {green_grass_total_energy} kkal \n"
            f"Total calories intakes: {total_energy} kkal")

bananas_weight = pw_input(f"Please enter how much grams of bananas \U0001F34C you want: \n"
                          f"Calories {BANANAS_KKAL} Kkal/100gr.", type=FLOAT)
bananas_total_energy = round(bananas_weight * BANANAS_KKAL / 100, 2)
total_energy += bananas_total_energy
put_success(f"You ordered {bananas_weight} grams of bananas \U0001F34C \n"
            f"Calories of portion: {bananas_total_energy} kkal \n"
            f"Total calories intakes: {total_energy} kkal")

waffles_weight = pw_input(f"Please enter how much grams of waffles \U0001F9C7 you want: \n"
                          f"Calories {WAFFLES_KKAL} Kkal/100gr.", type=FLOAT)
waffles_total_energy = round(waffles_weight * WAFFLES_KKAL / 100, 2)
total_energy += waffles_total_energy
put_success(f"You ordered {waffles_weight} grams of waffles \U0001F9C7 \n"
            f"Calories of portion: {waffles_total_energy} kkal \n"
            f"Total calories intakes: {total_energy} kkal")

grain_bread_first_class_weight = pw_input(f"Please enter how much grams of grain bread \U0001F956 you want: \n"
                                          f"Calories {GRAIN_BREAD_FIRST_CLASS_KKAL} Kkal/100gr.", type=FLOAT)
grain_bread_total_energy = round(grain_bread_first_class_weight * GRAIN_BREAD_FIRST_CLASS_KKAL / 100, 2)
total_energy += grain_bread_total_energy
put_success(f"You ordered {grain_bread_first_class_weight} grams of waffles \U0001F956 \n"
            f"Calories of portion: {grain_bread_total_energy} kkal \n"
            f"Total calories intakes: {total_energy} kkal")

pistachio_weight = pw_input(f"Please enter how much grams of pistachio \U0001F95C you want: \n"
                            f"Calories {PISTACHIO_KKAL} Kkal/100gr.", type=FLOAT)
pistachio_total_energy = round(pistachio_weight * PISTACHIO_KKAL / 100, 2)
total_energy += pistachio_total_energy
put_success(f"You ordered {pistachio_weight} grams of pistachio \U0001F95C \n"
            f"Calories of portion: {pistachio_total_energy} kkal \n"
            f"Total calories intakes: {total_energy} kkal")

kefir_25_weight = pw_input(f"Please enter how much grams of kefir \U0001F95B you want: \n"
                           f"Calories {KEFIR_25_KKAL} Kkal/100gr.", type=FLOAT)
kefir_total_energy = round(kefir_25_weight * KEFIR_25_KKAL / 100, 2)
total_energy += kefir_total_energy
put_success(f"You ordered {kefir_25_weight} grams of kefir \U0001F95B \n"
            f"Calories of portion: {kefir_total_energy} kkal \n"
            f"Total calories intakes: {total_energy} kkal")

if total_energy < 1000:
    put_warning('You, maybe will be hungry')
elif total_energy > 1500:
    put_warning('You cannot eat that much food')
else:
    put_success('Its very good choise for you')

total_bill_for_dinner = Decimal(total_energy * ONE_KKAL_PRICE).quantize(Decimal('0.01'))

put_success(f'Total bill for your dinner is: {total_bill_for_dinner} UAH')
