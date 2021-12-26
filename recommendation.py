def get_all_user_options(chk_options, ent_values):
    chk_checked_values = display_check_box_text_Value(chk_options)
    # TODO

def display_check_box_text_Value(chk_options):
    chk_checked_values = []

    if(chk_options[0].get() == 1):
        chk_checked_values.append("Romance")
    if(chk_options[1].get() == 1):
        chk_checked_values.append("History")
    if(chk_options[2].get() == 1):
        chk_checked_values.append("Nonfiction")
    if(chk_options[3].get() == 1):
        chk_checked_values.append("Fantasy")
    if(chk_options[4].get() == 1):
        chk_checked_values.append("Fiction")
    if(chk_options[5].get() == 1):
        chk_checked_values.append("Childrens")

    return chk_checked_values
