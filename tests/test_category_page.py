from config import BASE_URL


def test_category_opening(page):

    # Open main page
    from config import BASE_URL
    page.locator(".close-btn-block > .ic-close").dblclick()
    page.goto("https://missliberte-new.ffflabel-dev.com/shop-collection/")
    page.get_by_role("link", name="Swim", exact=True).click()
    page.goto("https://missliberte-new.ffflabel-dev.com/kategoria-produktu/miss-liberte-swim/")
    page.get_by_role("link", name="Bielizna").click()
    page.goto("https://missliberte-new.ffflabel-dev.com/kategoria-produktu/bielizna/")
    page.get_by_role("link", name="Biustonosze").click()
    page.goto("https://missliberte-new.ffflabel-dev.com/kategoria-produktu/biustonosze/")
    page.get_by_role("link", name="Majtki").click()
    page.goto("https://missliberte-new.ffflabel-dev.com/kategoria-produktu/majtki/")
    page.get_by_role("link", name="Body").click()
    page.goto("https://missliberte-new.ffflabel-dev.com/kategoria-produktu/body/")
    page.get_by_role("link", name="Homewear").click()
    page.goto("https://missliberte-new.ffflabel-dev.com/kategoria-produktu/homewear/")
    page.get_by_role("link", name="Sale").click()
    page.goto("https://missliberte-new.ffflabel-dev.com/kategoria-produktu/sale/")
    page.get_by_role("link", name="Karty podarunkowe").click()
    page.get_by_role("link", name="Last Pieces").click()
    page.goto("https://missliberte-new.ffflabel-dev.com/kategoria-produktu/last-pieces/")
    page.locator("#menu-item-22251").get_by_role("link", name="Kontakt").click()
    page.get_by_role("link", name="Dobierz rozmiar").click()
    page.get_by_role("link", name="Dostawy i płatności").dblclick()
    page.goto("https://missliberte-new.ffflabel-dev.com/dostawa-i-platnosci/")
    page.get_by_role("link", name="Wymiany i zwroty").click()
    page.get_by_role("link", name="Jak kupić na prezent").click()
    page.goto("https://missliberte-new.ffflabel-dev.com/na-prezent/")
    page.locator("#menu-item-23012").get_by_role("link", name="O Miss Liberté").click()
    page.goto("https://missliberte-new.ffflabel-dev.com/o-nas/")
    page.locator("#menu-item-22031").get_by_role("link", name="Zrównoważona produkcja").dblclick()
    page.goto("https://missliberte-new.ffflabel-dev.com/zrownowazona-produkcja/")
    page.locator("#menu-item-22032").get_by_role("link", name="Współpraca").click()
    page.get_by_role("link", name="MISS LIBERTÉ • Oficjalny").dblclick()
    page.goto("https://missliberte-new.ffflabel-dev.com/")

    # Open

