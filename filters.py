def filter_by_price(data, minimum_price):

    result = []

    for coin in data:

        try:
            price = (
                coin["Price"]
                .replace("$", "")
                .replace(",", "")
            )

            if float(price) >= minimum_price:
                result.append(coin)

        except:
            pass

    return result


def highest_gainer(data):

    highest = None
    highest_change = float("-inf")

    for coin in data:

        try:

            change = (
                coin["24h Change"]
                .replace("%", "")
                .replace(",", "")
            )

            change = float(change)

            if change > highest_change:

                highest_change = change
                highest = coin

        except:
            pass

    return highest