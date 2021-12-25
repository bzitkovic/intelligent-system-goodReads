attribute_names =  ['rating','totalratings', 'pages', 'reviews']

def predict_totalratings(rating=3.45, reviews=500):
    if (reviews is None):
        return 3057.92511
    if (reviews > 20929):
        return 865773.50602
    if (reviews <= 20929):
        if (reviews > 3864):
            if (reviews > 10467):
                return 257578.80909
            if (reviews <= 10467):
                return 102746.9724
        if (reviews <= 3864):
            if (reviews > 1029):
                if (reviews > 2071):
                    return 44819.62216
                if (reviews <= 2071):
                    if (reviews > 1451):
                        return 24992.91149
                    if (reviews <= 1451):
                        return 17208.31345
            if (reviews <= 1029):
                if (reviews > 293):
                    if (reviews > 603):
                        if (rating is None):
                            return 11155.58861
                        if (rating > 395):
                            return 13485.22924
                        if (rating <= 395):
                            return 9401.83862
                    if (reviews <= 603):
                        if (rating is None):
                            return 5795.94208
                        if (rating > 399):
                            return 7425.88305
                        if (rating <= 399):
                            return 4879.85266
                if (reviews <= 293):
                    return 534.21444


