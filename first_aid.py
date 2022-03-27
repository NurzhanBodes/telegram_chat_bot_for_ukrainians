from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

tournitext="""Injured limb \n
1. Wrap the triangular bandage (or strip of cloth) around the injured limb and cross over the ends. Slip the anti-pinch card underneath, pull the tight to hold in place. \n
2. Tie the Toni-key using knot to secure. \n
3. Twist the Tourni-key until the bleeding has stopped - this may hurt the casualty \n
4. Hook under the triangular bandage to lock it in place \n
5. Call 112/103"""
recovertext="""
“Recovery position \n
1. Place nearest arm at right angle \n
2. Put other hand next to check \n
3. Band far knee and roll them onto side \n
4. Open airway \n
5. Call 112/103”
"""

penetratingtext="""
“Penetrating Wounds \n
1. Press either side of the wound Do not remove the object \n
2. Build up padding either side of the object, so that it is taller than the object \n
3. Secure padding in place with a scarf or tie. \n
4. Call 112/103”
"""

gunshottext="""
“Gunshot wounds \n
1. Safety \n
2. Pack and press the wound \n
3. Lift the injured limb, if bleeding has not stopped use an improvised tourniquet  \n
4. Call 112/103”
"""

eyetext="""
Eye Injuries \n
1. Help the casualty to lie back and support their head. Tell them to keep both eyes still \n
2. Give them a dressing to hold over the eye and secure in place \n
3. Seek medical advice straight away
"""

burntext="""
Burns \n
1. Hold burn under cool running water for at least 20 minutes \n
2. Call 112/103 \n
3. Cover loosely with cling film or sterile dressing\n
4. Call 112/103
"""

amputationtext="""
Amputation  \n
1. Cover the wound with a dressing/ tea towel or t-shirt and press down. Lift the injured limp up if bleeding hasn’t stopped and use an improvised tourniquet e.g. a belt or scarf \n
2. Wrap the separated part in a plastic bag or cling film, then wrap in a soft material, e.g. t-shirt.  \n
3. Place in a bag go crushed ice \n
4. Call 112/103"""

tournitextu="""Пошкоджена кінцівка\n 
1. Оберніть трикутну пов'язку (або смужку тканини) навколо пошкодженої кінцівки і перехрестіть кінці. Вставте карту захисту від защемлення під неї, щільно затягніть їх, щоб зафіксувати на місці. \n
2. Зауважте тонік-ключ за допомогою вузла для закріплення. \n
3. Закручуйте джгут до тих пір, поки кровотеча не зупиниться - це може пошкодити потерпілому \n
4. Зачепіть гачок під трикутною пов'язкою, щоб зафіксувати її на місці \n
5. Зателефонуйте 112/103
"""
recovertextu="""
Положення відновлення \n
1. Розташуйте найближчий важіль під прямим кутом \n
2. Покладіть іншу руку поруч з галочкою \n
3. Перев'яжіть дальнє коліно і переверніть його на бік \n
4. Відкриті дихальні шляхи \n
5. Зателефонуйте 112/103"""
penetratingtextu="""Проникаючі поранення\n
1. Натисніть з обох сторін рани, не видаляйте об'єкт \n
2. Створіть відступи з обох сторін об'єкта, щоб він був вище, ніж об'єкт \n
3. Закріпіть прокладку на місці за допомогою шарфа або краватки. \n
4. Зателефонуйте 112/103
"""
gunshottextu="""
Вогнепальні поранення\n
1. Безпека \n
2. Упакуйте і притисніть рану \n
3. Підніміть пошкоджену кінцівку, якщо кровотеча не зупинилося, використовуйте імпровізований джгут \n
4. Зателефонуйте 112/103"""
eyetextu="""Травми очей \n
1. Допоможіть потерпілому лягти на спину і підтримати голову. Скажіть їм, щоб вони тримали обидва ока нерухомими \n
2. Дайте їм пов'язку, щоб тримати над оком і закріпити на місці \n
3. Негайно зверніться за медичною допомогою
"""
burntextu="""Опіки \n
1. Потримайте опік під прохолодною проточною водою не менше 20 хвилин \n
2. Зателефонуйте за номером 112/103 \n
3. Накрийте нещільно харчовою плівкою або стерильною пов'язкою\n
4. Зателефонуйте 112/103
"""
amputationtextu="""Ампутація \n
1. Накрийте рану пов'язкою / кухонним рушником або футболкою і притисніть. Підніміть потерпілого, якщо кровотеча не зупинилося, і використовуйте імпровізований джгут, наприклад, пояс або шарф \n
2. Загорніть відокремлену частину в пластиковий пакет або харчову плівку, потім загорніть в м'який матеріал, наприклад футболку. \n
3. Покладіть в пакет колотий лід \n
4. Зателефонуйте 112/103
"""
Tourni = InlineKeyboardButton(text="Injured limb", callback_data="tourni")
Recovery = InlineKeyboardButton(text="Recovery position", callback_data="recovery")
PenetratingW = InlineKeyboardButton(text="Penetrating Wounds", callback_data="penetrating")
GunshotW = InlineKeyboardButton(text="Gunshot Wounds",callback_data="gunshot")
Eyebutton = InlineKeyboardButton(text="Eye Wound",callback_data="eye")
Burnbutton=InlineKeyboardButton(text="Burns",callback_data="burn")
Amputationbutton=InlineKeyboardButton(text="Amputations",callback_data="amputation")

medhelp2=InlineKeyboardMarkup().add(Tourni).add(Recovery).add(PenetratingW).add(GunshotW).add(Eyebutton).add(Burnbutton).add(Amputationbutton)


Tourniu = InlineKeyboardButton(text="Пошкоджена кінцівка ", callback_data="tourniu")
Recoveryu = InlineKeyboardButton(text="Положення відновлення", callback_data="recoveryu")
PenetratingWu = InlineKeyboardButton(text="Проникаючі поранення", callback_data="penetratingu")
GunshotWu = InlineKeyboardButton(text="Вогнепальні поранення",callback_data="gunshotu")
Eyebuttonu = InlineKeyboardButton(text="Травми очей",callback_data="eyeu")
Burnbuttonu=InlineKeyboardButton(text="Опіки",callback_data="burnu")
Amputationbuttonu=InlineKeyboardButton(text="Ампутація ",callback_data="amputationu")
medhelpua=InlineKeyboardMarkup().add(Tourniu).add(Recoveryu).add(PenetratingWu).add(GunshotWu).add(Eyebuttonu).add(Burnbuttonu).add(Amputationbuttonu)
