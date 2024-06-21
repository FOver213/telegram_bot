from aiogram import F,Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message, CallbackQuery


from app.keyboards import ikb1

import app.keyboards as kb

router = Router()


@router.message(Command('help'))
async def cmd_start(message:Message):
    await message.reply('Привет, это бот-справочник, в котором будет информация о некоторых странах!')

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.reply(f'Привет!\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}',reply_markup=kb.rb1_reply)

#InLine
@router.message(Command('country'))
async def countrys(message: Message):
    await message.reply('Страны:',
                        reply_markup=kb.ikb1)

#Россия
@router.callback_query(F.data == 'russia')
async def Russia(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Россия', reply_markup=kb.ikb1_russia)

@router.callback_query(F.data == 'russia_gimn')
async def rus_gimn(callback: CallbackQuery):
    await callback.message.edit_text('Россия — священная наша держава,\nРоссия — любимая наша страна.\nМогучая воля, великая слава —\nТвое достояние на все времена!Ссылка на гимн https://www.chitalnya.ru/work/3070043/')

@router.callback_query(F.data == 'russia_stol')
async def rus_stol(callback: CallbackQuery):
    await callback.message.edit_text('Москва')

@router.callback_query(F.data == 'russia_gerb')
async def rus_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://pic.rutubelist.ru/video/7f/f2/7ff2fc80672d420e6e4ce2172296c5f1.jpg')

@router.callback_query(F.data == 'left')
async def lef_arrow(callback: CallbackQuery):
    await callback.message.edit_text('Страны:', reply_markup=kb.ikb1)

#Канада

@router.callback_query(F.data == 'kanada')
async def Kanada(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Канада', reply_markup=kb.ikb1_kanada)

@router.callback_query(F.data == 'kanada_stol')
async def rus_stol(callback: CallbackQuery):
    await callback.message.edit_text('Оттава')

@router.callback_query(F.data == 'kanada_gimn')
async def rus_stol(callback: CallbackQuery):
    await callback.message.edit_text('O, Канада! Наш Дом в Родной земле!\nЧистая любовь в сердцах твоих детей.\nhttps://wikiway.com/canada/gimn/')

@router.callback_query(F.data == 'kanada_gerb')
async def rus_stol(callback: CallbackQuery):
    await callback.message.edit_text('https://w7.pngwing.com/pngs/809/405/png-transparent-arms-of-canada-royal-coat-of-arms-of-the-united-kingdom-history-of-canada-canada-canada-maple-leaf-world.png')

#США

@router.callback_query(F.data == 'USA')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('USA', reply_markup=kb.ikb1_USA)

@router.callback_query(F.data == 'usa_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text('О, скажи, видишь ты в первых солнца лучах,\nЧто средь битвы мы шли на вечерней зарнице?\nhttps://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%BC%D0%BD_%D0%A1%D0%A8%D0%90')

@router.callback_query(F.data == 'usa_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Вашингтон')

@router.callback_query(F.data == 'usa_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://e7.pngegg.com/pngimages/567/289/png-clipart-usa-gerb-usa-gerb.png')

#Китай

@router.callback_query(F.data == 'china')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Китай', reply_markup=kb.ikb1_China)

@router.callback_query(F.data == 'china_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text('Вставай, кто рабом стать не желает!\nИз своей плоти Великую стену поставим!\nhttps://discoveric.ru/anthem/kitay')

@router.callback_query(F.data == 'china_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Пекин')

@router.callback_query(F.data == 'china_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://www.okaytravel.ru/wp-content/uploads/2023/07/gerb-kitaja.jpg')

#Бразилия


@router.callback_query(F.data == 'brazil')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Бразилия', reply_markup=kb.ikb1_Brazil)

@router.callback_query(F.data == 'braz_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text('Услышали Ипиранги-реки тихие берега\nГромоподобный клич героического народа\nhttps://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%BC%D0%BD_%D0%91%D1%80%D0%B0%D0%B7%D0%B8%D0%BB%D0%B8%D0%B8')

@router.callback_query(F.data == 'braz_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Бразилиа')

@router.callback_query(F.data == 'braz_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://w7.pngwing.com/pngs/27/485/png-transparent-empire-of-brazil-coat-of-arms-of-brazil-coat-of-arms-of-australia-brazil-rio-decorative-elements-flag-leaf-decorative.png')

#Австралия


@router.callback_query(F.data == 'avstraliya')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Бразилия', reply_markup=kb.ikb1_Avstraliya)

@router.callback_query(F.data == 'avstr_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text('Австралийцы, всё к счастью для нас\nЗдесь, где юность с свободой цветут.\nhttps://discoveric.ru/anthem/avstraliya')

@router.callback_query(F.data == 'avstr_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Канберра')

@router.callback_query(F.data == 'avstr_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://abali.ru/wp-content/uploads/2010/12/gerb_australia.png')

#Индия


@router.callback_query(F.data == 'indiya')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Индия', reply_markup=kb.ikb1_indiya)

@router.callback_query(F.data == 'ind_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text('Слава тебе — властителю дум всех народов,\nВершителю судьбы Индии\nhttps://discoveric.ru/anthem/indiya')

@router.callback_query(F.data == 'ind_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Нью-Дели')

@router.callback_query(F.data == 'ind_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://bumper-stickers.ru/54997-thickbox_default/gerb-emblema-indii.jpg')


#Аргентина


@router.callback_query(F.data == 'argentina')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Аргентина', reply_markup=kb.ikb1_argen)

@router.callback_query(F.data == 'argen_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text('Слушайте смертные! Крики священные:\nСвобода, Свобода, Свобода!\nhttps://discoveric.ru/anthem/argentina')

@router.callback_query(F.data == 'argen_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Буэнос-Айрес ')

@router.callback_query(F.data == 'argen_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://bellville.gob.ar/wp-content/uploads/2019/03/Escudo-Nacional.jpg')


#Казахстан


@router.callback_query(F.data == 'kazahstan')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Аргентина', reply_markup=kb.ikb1_kazah)

@router.callback_query(F.data == 'kazah_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text(' В её небе золотое солнце,\nВ её степях золотое зерно.\nhttps://discoveric.ru/anthem/kazahstan')

@router.callback_query(F.data == 'kazah_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Нур-Султан')

@router.callback_query(F.data == 'kazah_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://img.razrisyika.ru/kart/63/1200/248388-gerb-kazahstana-33.jpg')


#Алжир


@router.callback_query(F.data == 'alshir')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Алжир', reply_markup=kb.ikb1_alsh)

@router.callback_query(F.data == 'alsh_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text('Мы клянемся! Опустошительными бурями, охватившими нас\nЩедро пролитой благородной, чистой кровью\nhttps://discoveric.ru/anthem/alzhir')

@router.callback_query(F.data == 'alsh_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Алжир')

@router.callback_query(F.data == 'alsh_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://w7.pngwing.com/pngs/451/446/png-transparent-algeria-coat-of-arms-heraldry.png')





















