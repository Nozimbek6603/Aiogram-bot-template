from aiogram import Dispatcher
from loader import dp

from filters.AdminFilter import IsAdmin
from filters.GroupFilter import IsGroup
from filters.PrivateFilter import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
