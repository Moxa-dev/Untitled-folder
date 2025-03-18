# Определение персонажей
define mc = Character("Главный герой", color="#c8ffc8", image="mc")
define friend = Character("Однокурсник", color="#c8c8ff", image="friend")
define teacher = Character("Учитель", color="#ffc8c8", image="teacher")
define heroine = Character("Героиня", color="#ffc8ff", image="heroine")
define colleague = Character("Коллега А", color="#c8ffff", image="colleague")
define teammate = Character("Сокомандник А", color="#ffffc8", image="teammate")
define interviewer = Character("Интервьюер", color="#c8c8c8", image="interviewer")

# Инициализация переменных
default knowledge = 0
default programming_skill = 0
default data_analysis_skill = 0
default communication_skill = 0
default creativity = 0
default emotion = 0
default stress = 0
default observation_skill = 0  # Новая переменная для наблюдательности
default main_11_completed = False  # Флаг завершения основной линии 11

# Начало игры
label start:
    scene library with fade
    play music "audio/bgm_library.ogg" fadein 2.0
    show mc at left
    "В библиотеке было так тихо, что слышался шелест страниц. Солнечный свет пробивался сквозь высокие стеллажи, создавая на полу причудливые узоры."
    mc "Столько книг... С чего же мне начать?"
    
    show friend at right
    friend "Эй, тебе тоже интересна IT-сфера? Я думаю, это очень сложная, но перспективная область! Есть ли у тебя конкретные интересы?"
    
    menu:
        "Меня больше интересует программирование.":
            jump programming_path
        "Я склоняюсь к анализу данных и их обработке.":
            jump data_analysis_path
        "Я пока в раздумьях и не определился с направлением.":
            jump undecided_path

# ========== Основная линия 1: Программирование ==========
label programming_path:
    scene library_discussion with fade
    play music "audio/bgm_library.ogg" fadein 2.0
    show mc at left
    show friend at right
    mc "Программирование звучит круто, но я не знаю, с чего начать."
    friend "Программирование — это отличный выбор! Ты можешь начать с Python, он подходит для новичков. Кстати, на следующей неделе у нас будет лекция по программированию, хочешь пойти вместе?"
    
    menu:
        "Согласиться пойти на лекцию.":
            jump attend_lecture
        "Отказаться, решив сначала учиться самостоятельно.":
            jump attend_lecture

label attend_lecture:
    scene school_hall with fade
    play music "audio/bgm_school.ogg" fadein 2.0
    show mc at left
    "Зал был полон, и лектор, молодой программист, делился своим опытом."
    "Лектор: Программирование — это не просто написание кода, это способ мышления для решения проблем. Если вы будете упорны, то сможете стать отличным программистом."
    mc "Его слова вдохновили меня. Может, я действительно смогу попробовать."
    $ knowledge += 10
    $ programming_skill += 8
    $ communication_skill += 7
    
    menu:
        "Записаться в школьный клуб программирования.":
            jump join_programming_club
        "Начать учиться самостоятельно, составить план обучения.":
            jump self_learning_plan

label join_programming_club:
    scene club_room with fade
    play music "audio/bgm_school.ogg" fadein 2.0
    show mc at left
    show teammate at right
    "В комнате клуба стояли компьютеры и книги по программированию, несколько участников обсуждали проект."
    teammate "Мы разрабатываем небольшую игру, хочешь присоединиться?"
    
    menu:
        "С радостью присоединиться к разработке игры.":
            jump join_game_development
        "Отказаться, решив сначала изучить основы.":
            jump learn_basics

label join_game_development:
    scene club_room with fade
    play music "audio/bgm_school.ogg" fadein 2.0
    show mc at left
    show teammate at right
    "Главный герой присоединился к проекту и начал работать с командой."
    $ programming_skill += 10
    $ communication_skill += 8
    $ creativity += 7
    jump programming_competition_intro

label learn_basics:
    scene mc_room with fade
    play music "audio/bgm_library.ogg" fadein 2.0
    show mc at center
    "Главный герой решил сначала изучить основы и начал учиться самостоятельно."
    $ knowledge += 8
    $ programming_skill += 6
    jump programming_competition_intro

label self_learning_plan:
    scene mc_room with fade
    play music "audio/bgm_library.ogg" fadein 2.0
    show mc at center
    "Главный герой сел за стол, включил компьютер и начал искать учебные материалы."
    mc "Начну с основ Python, буду учиться по два часа в день и посмотрю, что получится через месяц."
    $ knowledge += 8
    $ programming_skill += 6
    
    menu:
        "Продолжать учиться и завершить первый проект.":
            jump complete_project
        "Столкнуться с трудностями и замедлить прогресс.":
            jump slow_down_progress

label complete_project:
    scene mc_room with fade
    play music "audio/bgm_library.ogg" fadein 2.0
    show mc at center
    "Главный герой завершил свой первый проект — простой калькулятор."
    $ programming_skill += 10
    $ creativity += 8
    jump programming_competition_intro

label slow_down_progress:
    scene mc_room with fade
    play music "audio/bgm_library.ogg" fadein 2.0
    show mc at center
    "Главный герой столкнулся с трудностями и решил замедлить темп обучения, чтобы лучше понять сложные концепции."
    $ stress -= 5
    jump programming_competition_intro

# ========== Основная линия 2: Анализ данных ==========
label data_analysis_path:
    scene library_data with fade
    play music "audio/bgm_library.ogg" fadein 2.0
    show mc at left
    show friend at right
    mc "Анализ данных, кажется, может быть полезен во многих отраслях."
    friend "Анализ данных — это действительно перспективное направление! Ты можешь начать с Excel и SQL. Кстати, у меня есть друг, который стажируется в этой области, хочешь, я спрошу у него?"
    
    menu:
        "Попросить однокурсника помочь с поиском стажировки.":
            jump ask_for_internship
        "Отказаться, решив сначала учиться самостоятельно.":
            jump self_study_data

label ask_for_internship:
    scene data_company with fade
    play music "audio/bgm_office.ogg" fadein 2.0
    show mc at left
    show interviewer at right
    "Главный герой пришел в компанию по анализу данных на собеседование."
    interviewer "Что ты знаешь об анализе данных? Можешь кратко рассказать?"
    
    menu:
        "Уверенно ответить, показав свои знания.":
            jump confident_answer
        "Честно признаться, что еще учится, но готов стараться.":
            jump honest_answer

label confident_answer:
    scene data_company with fade
    play music "audio/bgm_office.ogg" fadein 2.0
    show mc at left
    show interviewer at right
    interviewer "Отлично, у тебя хорошая база. Добро пожаловать в нашу команду!"
    $ knowledge += 12
    $ data_analysis_skill += 10
    $ communication_skill += 8
    jump internship_experience

label honest_answer:
    scene data_company with fade
    play music "audio/bgm_office.ogg" fadein 2.0
    show mc at left
    show interviewer at right
    interviewer "Хорошо, мы ценим твою честность и старательность. Добро пожаловать в команду!"
    $ knowledge += 10
    $ data_analysis_skill += 8
    $ communication_skill += 6
    jump internship_experience

label self_study_data:
    scene mc_room with fade
    play music "audio/bgm_library.ogg" fadein 2.0
    show mc at center
    "Главный герой решил сначала изучить основы анализа данных самостоятельно."
    $ knowledge += 8
    $ data_analysis_skill += 6
    jump internship_experience

# ========== Основная линия 3: Консультация с учителем ==========
label undecided_path:
    scene teacher_office with fade
    play music "audio/bgm_library.ogg" fadein 2.0
    show mc at left
    show teacher at right
    "В кабинете учителя было много книг и документов. Учитель сидел за столом и улыбался."
    teacher "Студент, IT-сфера — это хороший выбор, но тебе нужно учитывать свои интересы и способности. Ты уверен в своих логических и творческих способностях?"
    
    menu:
        "Я уверен в своих логических и творческих способностях.":
            jump confident_in_logic
        "Мне кажется, мои логические способности нужно улучшить.":
            jump improve_logic
        "Я не уверен, есть ли у меня такие способности.":
            jump unsure_abilities

label confident_in_logic:
    scene teacher_office with fade
    play music "audio/bgm_library.ogg" fadein 2.0
    show mc at left
    show teacher at right
    teacher "Отлично! Я советую тебе начать с основ и постепенно развиваться. В школе скоро будет конкурс по программированию, хочешь поучаствовать?"
    
    menu:
        "Записаться на конкурс по программированию.":
            jump join_programming_competition
        "Отказаться, решив сначала сосредоточиться на учебе.":
            jump focus_on_studies

label improve_logic:
    scene teacher_office with fade
    play music "audio/bgm_library.ogg" fadein 2.0
    show mc at left
    show teacher at right
    "Учитель кивнул, казалось, он был доволен честностью главного героя."
    teacher "Логическое мышление можно развить с помощью практики. Начни с решения простых задач и постепенно усложняй."
    mc "Спасибо за совет, я постараюсь."
    $ knowledge += 5
    $ programming_skill += 5
    jump focus_on_studies

label unsure_abilities:
    scene teacher_office with fade
    play music "audio/bgm_library.ogg" fadein 2.0
    show mc at left
    show teacher at right
    "Учитель мягко улыбнулся, понимая сомнения главного героя."
    teacher "Ничего страшного, многие сначала не уверены, подходит ли им эта сфера. Ты можешь начать с базовых курсов и посмотреть, интересно ли тебе."
    mc "Спасибо за совет, я попробую."
    $ knowledge += 5
    jump focus_on_studies

label join_programming_competition:
    scene competition_venue with fade
    play music "audio/bgm_competition.ogg" fadein 2.0
    show mc at left
    show teammate at right
    "На конкурсе царила напряженная атмосфера, главный герой и его команда обсуждали решение задачи."
    teammate "Эта задача сложная, нам нужно поторопиться!"
    
    menu:
        "Предложить свое решение.":
            jump propose_solution
        "Послушать совет команды и изменить стратегию.":
            jump follow_teammate_advice

label propose_solution:
    scene cafe with fade
    play music "audio/bgm_competition.ogg" fadein 2.0
    show mc at left
    show teammate at right
    teammate "Твое решение звучит неплохо, давай попробуем!"
    $ knowledge += 10
    $ programming_skill += 8
    $ communication_skill += 6
    jump programming_competition_result

label follow_teammate_advice:
    scene competition_venue with fade
    play music "audio/bgm_competition.ogg" fadein 2.0
    show mc at left
    show teammate at right
    "Главный герой последовал совету команды и изменил стратегию."
    $ programming_skill += 6
    $ communication_skill += 8
    jump programming_competition_result

label focus_on_studies:
    scene mc_room with fade
    play music "audio/bgm_library.ogg" fadein 2.0
    show mc at center
    "Главный герой решил сосредоточиться на учебе и укрепить свои знания."
    $ knowledge += 8
    $ programming_skill += 6
    jump programming_competition_result

# ========== Результаты конкурса по программированию ==========
label programming_competition_result:
    scene competition_venue with fade
    play music "audio/bgm_competition.ogg" fadein 2.0
    show mc at left
    show teammate at right
    "Конкурс завершился, главный герой и его команда вздохнули с облегчением."
    $ knowledge += 10
    $ programming_skill += 8
    $ communication_skill += 6
    jump internship_experience

# ========== Основная линия 4: Первый опыт стажировки ==========
label internship_experience:
    scene data_company_office with fade
    play music "audio/bgm_office.ogg" fadein 2.0
    show mc at left
    show colleague at right
    "Главный герой в первый день стажировки в компании по анализу данных. В офисе царила напряженная атмосфера, коллеги обсуждали важный проект."
    colleague "Добро пожаловать в команду! Мы анализируем данные клиента, хочешь присоединиться?"
    
    menu:
        "Активно участвовать и предложить свои идеи.":
            jump active_participation
        "Сначала понаблюдать и учиться, затем участвовать.":
            jump observe_and_learn
        "Отказаться, сказав, что еще адаптируется.":
            jump decline_participation

label active_participation:
    scene meeting_room with fade
    play music "audio/bgm_office.ogg" fadein 2.0
    show mc at left
    show colleague at right
    "Главный герой и коллеги сидели за столом, на экране отображались результаты анализа."
    mc "Я думаю, мы можем начать с анализа поведения пользователей и их привычек."
    colleague "Хорошая идея! Давай попробуем."
    $ data_analysis_skill += 10
    $ communication_skill += 8
    $ creativity += 7
    
    menu:
        "Продолжить углубленный анализ и предложить больше идей.":
            jump deeper_analysis
        "Сделать перерыв и привести мысли в порядок.":
            jump take_a_break

label deeper_analysis:
    scene data_analysis_desk with fade
    play music "audio/bgm_office.ogg" fadein 2.0
    show mc at center
    "Главный герой сидел за компьютером, углубившись в анализ данных, и вдруг обнаружил интересную тенденцию."
    mc "Я нашел потенциальную рыночную возможность!"
    colleague "Отличная работа! Это открытие очень полезно для нашего проекта."
    $ data_analysis_skill += 12
    $ creativity += 10
    jump internship_conclusion

label take_a_break:
    scene data_company_office with fade
    play music "audio/bgm_office.ogg" fadein 2.0
    show mc at center
    "Главный герой решил сделать перерыв и привести свои мысли в порядок."
    $ stress -= 5
    jump internship_conclusion

label observe_and_learn:
    scene data_company_office with fade
    play music "audio/bgm_office.ogg" fadein 2.0
    show mc at center
    "Главный герой сидел за своим рабочим местом, внимательно наблюдая за коллегами."
    mc "Их методы работы очень эффективны, мне нужно научиться у них."
    $ knowledge += 8
    $ observation_skill += 6
    
    menu:
        "Попросить совета у коллег.":
            jump ask_for_advice
        "Продолжать наблюдать и ждать подходящего момента для участия.":
            jump continue_observing

label ask_for_advice:
    scene break_room with fade
    play music "audio/bgm_office.ogg" fadein 2.0
    show mc at left
    show colleague at right
    "Главный герой и коллега разговаривали в комнате отдыха, главный герой воспользовался моментом, чтобы задать вопросы."
    colleague "Ключ к анализу данных — найти их ценность, а не просто анализировать."
    mc "Спасибо за совет, я запомню."
    $ knowledge += 10
    $ communication_skill += 8
    jump internship_conclusion

label continue_observing:
    scene data_company_office with fade
    play music "audio/bgm_office.ogg" fadein 2.0
    show mc at center
    "Главный герой решил продолжать наблюдать и ждать подходящего момента для участия."
    $ knowledge += 6
    $ observation_skill += 8
    jump internship_conclusion

label decline_participation:
    scene data_company_office with fade
    play music "audio/bgm_office.ogg" fadein 2.0
    show mc at center
    "Главный герой отказался от предложения коллег, сказав, что еще адаптируется."
    $ stress -= 5
    jump internship_conclusion

# ========== Итоги стажировки ==========
label internship_conclusion:
    scene data_company_office with fade
    play music "audio/bgm_office.ogg" fadein 2.0
    show mc at center
    "После стажировки главный герой набрался опыта и глубже понял анализ данных."
    $ knowledge += 15
    $ data_analysis_skill += 12
    $ communication_skill += 10
    jump programming_competition_intro

# ========== Основная линия 5: Соревнование по программированию ==========
label programming_competition_intro:
    scene competition_venue with fade
    play music "audio/bgm_competition.ogg" fadein 2.0
    show mc at left
    show teammate at right
    "Главный герой и его команда решали сложную задачу, время поджимало."
    teammate "Эта задача сложная, нам нужно поторопиться!"
    
    menu:
        "Спокойно проанализировать и предложить новое решение.":
            jump calm_analysis
        "Послушать совет команды и продолжить текущий метод.":
            jump follow_teammate_advice_competition
        "Сделать перерыв и привести мысли в порядок.":
            jump take_a_break_competition

label calm_analysis:
    scene cafe with fade
    play music "audio/bgm_competition.ogg" fadein 2.0
    show mc at left
    show teammate at right
    "Главный герой нарисовал решение на доске, команда внимательно слушала."
    mc "Если мы используем динамическое программирование, то сможем быстрее найти ответ."
    teammate "Звучит разумно, давай попробуем!"
    $ programming_skill += 10
    $ communication_skill += 8
    $ creativity += 7
    
    menu:
        "Продолжить оптимизацию решения.":
            jump optimize_solution
        "Отправить ответ и ждать результатов.":
            jump submit_solution

label optimize_solution:
    scene competition_venue with fade
    play music "audio/bgm_competition.ogg" fadein 2.0
    show mc at center
    "Главный герой и команда быстро печатали, оптимизируя код."
    mc "Мы сделали это! Код стал работать быстрее!"
    $ programming_skill += 12
    $ creativity += 10
    jump competition_conclusion

label submit_solution:
    scene competition_venue with fade
    play music "audio/bgm_competition.ogg" fadein 2.0
    show mc at left
    show teammate at right
    "Главный герой и команда отправили ответ и ждали результатов."
    $ programming_skill += 8
    $ communication_skill += 6
    jump competition_conclusion

label follow_teammate_advice_competition:
    scene competition_venue with fade
    play music "audio/bgm_competition.ogg" fadein 2.0
    show mc at left
    show teammate at right
    "Главный герой последовал совету команды и продолжил текущий метод."
    $ programming_skill += 6
    $ communication_skill += 8
    jump competition_conclusion

label take_a_break_competition:
    scene competition_venue with fade
    play music "audio/bgm_competition.ogg" fadein 2.0
    show mc at center
    "Главный герой решил сделать перерыв и привести свои мысли в порядок."
    $ stress -= 5
    jump competition_conclusion

# ========== Итоги соревнования ==========
label competition_conclusion:
    scene competition_venue with fade
    play music "audio/bgm_competition.ogg" fadein 2.0
    show mc at left
    show teammate at right
    "Соревнование завершилось, главный герой и команда вздохнули с облегчением."
    $ knowledge += 10
    $ programming_skill += 8
    $ communication_skill += 6
    jump ending

# ========== Основная линия 6: Ночной разговор с героиней ==========
label ending:
    scene lakeside_night with fade
    play music "audio/bgm_lakeside.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Ночью у озера было тихо и красиво, лунный свет отражался на воде. Героиня и главный герой сидели на скамейке, тихо разговаривая."
    heroine "Ты выглядишь уставшим, работа слишком напряженная?"
    mc "Да, стажировка и соревнования выматывают."
    
    menu:
        "Поделиться своими переживаниями и попросить поддержки.":
            jump vent_stress
        "Сделать вид, что все в порядке.":
            jump pretend_strength
        "Сменить тему и поговорить о чем-то легком.":
            jump change_topic

label vent_stress:
    scene lakeside_night with fade
    play music "audio/bgm_lakeside.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой рассказал героине о своих переживаниях и трудностях."
    heroine "Ты уже много сделал, не дави на себя слишком сильно. Помни, я всегда рядом."
    mc "Спасибо, с тобой все становится легче."
    $ emotion += 10
    $ stress -= 8
    
    menu:
        "Обнять героиню и выразить благодарность.":
            jump hug_heroine
        "Продолжить разговор, поделиться больше.":
            jump daily_life

label hug_heroine:
    scene lakeside_night with fade
    play music "audio/bgm_lakeside.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой обнял героиню, и они тихо наслаждались моментом."
    heroine "Что бы ни случилось, я всегда буду тебя поддерживать."
    $ emotion += 12
    $ stress -= 10
    jump daily_life

label continue_talking:
    scene lakeside_night with fade
    play music "audio/bgm_lakeside.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой и героиня продолжили разговор, делясь своими мыслями."
    $ emotion += 8
    $ stress -= 6
    jump daily_life

label pretend_strength:
    scene lakeside_night with fade
    play music "audio/bgm_lakeside.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой сделал вид, что все в порядке."
    $ stress += 5
    jump daily_life

label change_topic:
    scene lakeside_night with fade
    play music "audio/bgm_lakeside.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой сменил тему и заговорил о чем-то легком."
    $ stress -= 3
    jump daily_life

# ========== Основная линия 8: Повседневная жизнь с героиней ==========
label daily_life:
    scene mc_room with fade
    play music "audio/bgm_home.ogg" fadein 2.0
    show mc at center
    "Главный герой сидел за столом, готовясь к работе. Вдруг зазвонил телефон — это была героиня."
    heroine "У тебя есть время сегодня? Я хочу показать тебе одно место."

    menu:
        "Согласиться на приглашение героини.":
            jump explore_new_place
        "Отказаться, сказав, что нужно работать.":
            jump decline_explore

label explore_new_place:
    scene park with fade
    play music "audio/bgm_park.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой и героиня пришли в красивый городской парк. Солнце светило на траву, в воздухе витал аромат цветов."
    heroine "Это одно из моих любимых мест, здесь я всегда чувствую себя лучше."
    mc "Действительно красиво, здесь так спокойно."
    $ stress -= 10
    $ emotion += 10

    "Они гуляли по парку, и героиня вдруг остановилась, указывая на цветущее поле."
    heroine "Смотри, как красиво цветут эти цветы."

    menu:
        "Предложить сфотографироваться на память.":
            jump take_photos
        "Продолжить гулять, наслаждаясь моментом.":
            jump continue_walk

label take_photos:
    scene park_flowers with fade
    play music "audio/bgm_park.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой и героиня подошли к цветам, и героиня достала телефон."
    heroine "Давай сфотографируемся на память."
    mc "Конечно, с удовольствием."
    $ emotion += 10

    "Они сделали несколько фото, и героиня улыбнулась, глядя на них."
    heroine "Фотографии получились замечательные, я их сохраню."
    $ emotion += 5

    menu:
        "Предложить приходить сюда чаще.":
            jump suggest_regular_visits
        "Поблагодарить героиню за этот день.":
            jump thank_heroine

label suggest_regular_visits:
    scene park_flowers with fade
    play music "audio/bgm_park.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой улыбнулся и сказал:"
    mc "Может, будем приходить сюда чаще? Это будет наше секретное место."
    heroine "Отличная идея, я буду ждать."
    $ emotion += 10

    "Они продолжили гулять, и героиня вдруг остановилась, серьезно глядя на главного героя."
    heroine "На самом деле, у меня есть вопрос."

    menu:
        "Позволить героине задать вопрос.":
            jump ask_question_park
        "Пошутить и сменить тему.":
            jump change_topic_park

label ask_question_park:
    scene park_flowers with fade
    play music "audio/bgm_park.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Героиня глубоко вздохнула, казалось, она нервничала."
    heroine "Как ты думаешь, наши отношения... могут стать чем-то большим?"
    mc "Я..."

    menu:
        "Признаться в своих чувствах.":
            jump confess_feelings_park
        "Сказать, что нужно больше времени.":
            jump hesitate_park

label confess_feelings_park:
    scene park_flowers with fade
    play music "audio/bgm_park.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой взял героиню за руку и серьезно сказал:"
    mc "На самом деле, я давно думал об этом. Ты мне очень нравишься, и я хочу быть с тобой."
    heroine "Правда? Я так рада это слышать."
    $ emotion += 20

    "Они улыбнулись друг другу, и мир вокруг словно стал ярче."
    heroine "Тогда давай вместе справляться со всеми трудностями, хорошо?"
    mc "Хорошо, мы справимся."
    $ emotion += 10
    $ stress -= 10
    jump final_ending

label hesitate_park:
    scene park_flowers with fade
    play music "audio/bgm_park.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой немного замялся и тихо сказал:"
    mc "Мне нужно еще немного времени, чтобы разобраться в своих чувствах."
    heroine "Ничего страшного, я подожду."
    $ emotion += 5
    $ stress += 5

    "Героиня немного расстроилась, но все же улыбнулась и похлопала главного героя по плечу."
    heroine "Как бы ты ни решил, я всегда буду тебя поддерживать."
    $ emotion += 5
    jump final_ending

label change_topic_park:
    scene park_flowers with fade
    play music "audio/bgm_park.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой улыбнулся и попытался разрядить обстановку."
    mc "Сейчас задавать такие вопросы слишком серьезно, давай лучше продолжим гулять."
    heroine "Ладно, ты всегда умеешь сменить тему."
    $ emotion += 5

    "Они продолжили гулять, и хотя атмосфера была немного напряженной, героиня не казалась обиженной."
    heroine "Но однажды я все же получу ответ."
    $ emotion += 5
    jump final_ending

label thank_heroine:
    scene park_flowers with fade
    play music "audio/bgm_park.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой улыбнулся и сказал:"
    mc "Спасибо, что привела меня сюда, сегодня было действительно здорово."
    heroine "Не за что, мне тоже было приятно."
    $ emotion += 10

    "Они продолжили гулять, и героиня вдруг остановилась, серьезно глядя на главного героя."
    heroine "На самом деле, у меня есть вопрос."

    menu:
        "Позволить героине задать вопрос.":
            jump ask_question_park
        "Пошутить и сменить тему.":
            jump change_topic_park

label continue_walk:
    scene park with fade
    play music "audio/bgm_park.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Они продолжили гулять, наслаждаясь моментом."
    heroine "С тобой мне всегда спокойно."
    $ emotion += 10

    "Героиня вдруг остановилась, серьезно глядя на главного героя."
    heroine "На самом деле, у меня есть вопрос."

    menu:
        "Позволить героине задать вопрос.":
            jump ask_question_park
        "Пошутить и сменить тему.":
            jump change_topic_park

label decline_explore:
    scene mc_room with fade
    play music "audio/bgm_home.ogg" fadein 2.0
    show mc at center
    "Главный герой с сожалением посмотрел на экран телефона."
    mc "Извини, у меня много работы, я не смогу пойти."
    heroine "Ничего страшного, работа важнее. Когда освободишься, мы сходим."
    $ emotion += 5
    $ stress += 5

    "Героиня немного расстроилась, но все же улыбнулась."
    heroine "Не забывай заботиться о себе, не перетруждайся."
    $ emotion += 5
    jump final_ending

# ========== Основная линия 9: Планы на будущее с героиней ==========
label future_plan:
    scene mc_room with fade
    play music "audio/bgm_home.ogg" fadein 2.0
    show mc at center
    "Главный герой сидел за столом, размышляя о будущем. Вдруг зазвонил телефон — это была героиня."
    heroine "Ты думал о будущем? Может, обсудим?"

    menu:
        "Согласиться обсудить будущее.":
            jump discuss_future
        "Отказаться, сказав, что еще не определился.":
            jump decline_discuss

label discuss_future:
    scene cafe with fade
    play music "audio/bgm_cafe.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой и героиня пришли в кафе, заказали кофе и начали обсуждать будущее."
    heroine "Думаю, мы можем составить план, чтобы понять, куда двигаться."
    mc "Хорошая идея, я тоже об этом думал."
    $ emotion += 10
    $ stress -= 5

    "Они начали обсуждать свои карьерные и жизненные цели."
    heroine "Я планирую продолжить учебу, получить магистерскую степень. А ты?"

    menu:
        "Сказать, что тоже хочет продолжить учебу.":
            jump pursue_degree
        "Сказать, что хочет начать работать.":
            jump enter_workforce

label pursue_degree:
    scene cafe with fade
    play music "audio/bgm_cafe.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой улыбнулся и сказал:"
    mc "Я тоже думаю о продолжении учебы, может, мы поступим в один университет?"
    heroine "Правда? Это замечательно, мы сможем поддерживать друг друга."
    $ emotion += 15

    "Они начали обсуждать детали поступления, и героиня казалась очень взволнованной."
    heroine "Мы можем вместе готовиться к экзаменам, помогать друг другу."
    $ emotion += 10

    menu:
        "Предложить составить учебный план.":
            jump create_study_plan
        "Поблагодарить героиню за поддержку.":
            jump thank_support

label create_study_plan:
    scene cafe with fade
    play music "audio/bgm_cafe.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой достал блокнот и начал составлять учебный план."
    mc "Мы можем учиться вместе, поддерживать друг друга."
    heroine "Отличная идея, мы сможем добиться успеха."
    $ emotion += 10
    $ knowledge += 10

    "Они составили план, и героиня улыбнулась."
    heroine "С тобой мне все кажется проще."
    $ emotion += 10
    jump final_ending

label thank_support:
    scene cafe with fade
    play music "audio/bgm_cafe.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой с благодарностью посмотрел на героиню."
    mc "Спасибо за поддержку, я постараюсь."
    heroine "Я верю в тебя, мы справимся."
    $ emotion += 10

    "Они продолжили обсуждать будущее, и атмосфера была очень теплой."
    heroine "Что бы ни случилось, я всегда буду рядом."
    $ emotion += 10
    jump final_ending

label enter_workforce:
    scene cafe with fade
    play music "audio/bgm_cafe.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой серьезно сказал:"
    mc "Я хочу начать работать, набраться опыта."
    heroine "Это тоже хороший выбор, я поддержу твое решение."
    $ emotion += 10

    "Они начали обсуждать карьерные перспективы, и героиня казалась очень заинтересованной."
    heroine "Если тебе понадобится помощь, просто скажи."
    $ emotion += 10

    menu:
        "Поблагодарить героиню за поддержку.":
            jump thank_support_work
        "Предложить вместе справляться с трудностями.":
            jump face_challenges_together

label thank_support_work:
    scene cafe with fade
    play music "audio/bgm_cafe.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой с благодарностью посмотрел на героиню."
    mc "Спасибо за поддержку, я постараюсь."
    heroine "Я верю в тебя, мы справимся."
    $ emotion += 10

    "Они продолжили обсуждать будущее, и атмосфера была очень теплой."
    heroine "Что бы ни случилось, я всегда буду рядом."
    $ emotion += 10
    jump final_ending

label face_challenges_together:
    scene cafe with fade
    play music "audio/bgm_cafe.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой улыбнулся и сказал:"
    mc "Мы можем вместе справляться с трудностями, поддерживать друг друга."
    heroine "Отличная идея, мы справимся."
    $ emotion += 15

    "Они начали обсуждать карьерные перспективы, и героиня казалась очень взволнованной."
    heroine "С тобой мне все кажется проще."
    $ emotion += 10
    jump final_ending

label decline_discuss:
    scene mc_room with fade
    play music "audio/bgm_home.ogg" fadein 2.0
    show mc at center
    "Главный герой с сожалением посмотрел на экран телефона."
    mc "Извини, я еще не определился с будущим."
    heroine "Ничего страшного, мы можем обсудить позже. Когда решишь, дай знать."
    $ emotion += 5
    $ stress += 5

    "Героиня немного расстроилась, но все же улыбнулась."
    heroine "Не забывай заботиться о себе, не перетруждайся."
    $ emotion += 5
    jump final_ending

# ========== Основная линия 10: Совместное преодоление трудностей ==========
label face_challenges:
    scene mc_room with fade
    play music "audio/bgm_home.ogg" fadein 2.0
    show mc at center
    "Главный герой готовился к важному проекту, когда ему позвонила героиня."
    heroine "Я слышала, у тебя важный проект, нужна помощь?"

    menu:
        "Принять помощь героини.":
            jump accept_help
        "Отказаться, сказав, что справится сам.":
            jump decline_help

label accept_help:
    scene mc_room with fade
    play music "audio/bgm_home.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Героиня пришла к главному герою, и они начали готовиться к проекту."
    heroine "Мы можем разделить задачи, так будет быстрее."
    mc "Спасибо, с тобой мне легче."
    $ emotion += 10
    $ stress -= 10

    "Они начали работать, героиня занималась сбором данных, а главный герой — разработкой плана."
    heroine "Думаю, этот план можно улучшить, как считаешь?"

    menu:
        "Принять совет героини и улучшить план.":
            jump optimize_plan
        "Оставить план как есть, уверенный в своем решении.":
            jump stick_to_plan

label optimize_plan:
    scene mc_room with fade
    play music "audio/bgm_home.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой принял совет героини и начал улучшать план."
    mc "Твой совет очень полезен, я внесу изменения."
    heroine "Рада, что смогла помочь, мы справимся."
    $ emotion += 10
    $ knowledge += 10

    "Они продолжили работать, и проект продвигался успешно."
    heroine "С тобой мне все кажется проще."
    $ emotion += 10
    jump final_ending

label stick_to_plan:
    scene mc_room with fade
    play music "audio/bgm_home.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой улыбнулся и сказал:"
    mc "Я уверен в своем плане, но спасибо за совет."
    heroine "Ничего страшного, я верю в тебя."
    $ emotion += 5

    "Они продолжили работать, и проект продвигался успешно."
    heroine "С тобой мне все кажется проще."
    $ emotion += 10
    jump final_ending

label decline_help:
    scene mc_room with fade
    play music "audio/bgm_home.ogg" fadein 2.0
    show mc at center
    "Главный герой с сожалением посмотрел на экран телефона."
    mc "Извини, я хочу справиться сам."
    heroine "Ничего страшного, я верю в тебя. Если понадобится помощь, дай знать."
    $ emotion += 5
    $ stress += 5

    "Героиня немного расстроилась, но все же улыбнулась."
    heroine "Не забывай заботиться о себе, не перетруждайся."
    $ emotion += 5
    jump final_ending

# ========== Основная линия 11: Выпускной ==========
label graduation:
    scene school_hall with fade
    play music "audio/bgm_school.ogg" fadein 2.0
    show mc at center
    "Наступил день выпускного, зал был полон, главный герой и его однокурсники готовились к важному моменту."
    mc "Наконец-то этот день настал, все кажется сном."

    menu:
        "Найти героиню и разделить с ней этот момент.":
            jump find_heroine
        "Насладиться выпускным в одиночестве.":
            jump enjoy_alone

label find_heroine:
    scene school_hall with fade
    play music "audio/bgm_school.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой нашел героиню в толпе и подошел к ней."
    mc "Наконец-то нашел тебя, давай отпразднуем вместе."
    heroine "Конечно, сегодня особенный день."
    $ emotion += 10

    "Они сели в зале, ожидая начала церемонии."
    heroine "Ты помнишь, как мы впервые встретились?"

    menu:
        "Вспомнить первую встречу.":
            jump recall_first_meeting
        "Пошутить и сменить тему.":
            jump change_topic_graduation

label recall_first_meeting:
    scene school_hall with fade
    play music "audio/bgm_school.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой улыбнулся, вспоминая первую встречу."
    mc "Конечно помню, ты помогла мне найти книгу в библиотеке, и мы долго разговаривали."
    heroine "Да, мы были такими наивными."
    $ emotion += 10

    "Они продолжили вспоминать прошлое, и атмосфера была очень теплой."
    heroine "С тобой мне все кажется более значимым."
    $ emotion += 10

    menu:
        "Признаться героине в своих чувствах.":
            jump confess_feelings_graduation
        "Продолжить вспоминать, наслаждаясь моментом.":
            jump continue_recall

label confess_feelings_graduation:
    scene school_hall with fade
    play music "audio/bgm_school.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой взял героиню за руку и серьезно сказал:"
    mc "На самом деле, я давно хотел сказать, что ты для меня очень важна."
    heroine "Правда? Я так рада это слышать."
    $ emotion += 20

    "Они улыбнулись друг другу, и мир вокруг словно стал ярче."
    heroine "Тогда давай вместе справляться со всеми трудностями, хорошо?"
    mc "Хорошо, мы справимся."
    $ emotion += 10
    $ stress -= 10
    jump final_ending

label continue_recall:
    scene school_hall with fade
    play music "audio/bgm_school.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Они продолжили вспоминать прошлое, и атмосфера была очень теплой."
    heroine "С тобой мне все кажется более значимым."
    $ emotion += 10

    "Церемония началась, и они вместе поднялись на сцену, чтобы получить дипломы."
    $ knowledge += 20
    $ emotion += 10
    jump final_ending

label change_topic_graduation:
    scene school_hall with fade
    play music "audio/bgm_school.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой улыбнулся и попытался разрядить обстановку."
    mc "Сейчас вспоминать слишком серьезно, давай насладимся моментом."
    heroine "Ладно, ты всегда умеешь сменить тему."
    $ emotion += 5

    "Церемония началась, и они вместе поднялись на сцену, чтобы получить дипломы."
    $ knowledge += 20
    $ emotion += 5
    jump final_ending

label enjoy_alone:
    scene school_hall with fade
    play music "audio/bgm_school.ogg" fadein 2.0
    show mc at center
    "Главный герой сидел в зале один, наслаждаясь моментом."
    mc "Наконец-то этот день настал, все кажется сном."
    $ knowledge += 20

    "Церемония началась, и главный герой поднялся на сцену, чтобы получить диплом."
    $ knowledge += 10

    menu:
        "После церемонии найти героиню.":
            jump find_heroine_after
        "Уйти один, наслаждаясь тишиной.":
            jump leave_alone

label find_heroine_after:
    scene school_hall with fade
    play music "audio/bgm_school.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Главный герой нашел героиню после церемонии и подошел к ней."
    mc "Наконец-то нашел тебя, давай отпразднуем вместе."
    heroine "Конечно, сегодня особенный день."
    $ emotion += 10

    "Они вышли из зала, наслаждаясь моментом."
    heroine "С тобой мне все кажется более значимым."
    $ emotion += 10

    menu:
        "Признаться героине в своих чувствах.":
            jump confess_feelings_graduation
        "Продолжить наслаждаться моментом.":
            jump continue_graduation

label continue_graduation:
    scene school_hall with fade
    play music "audio/bgm_school.ogg" fadein 2.0
    show mc at left
    show heroine at right
    "Они продолжили наслаждаться моментом, и атмосфера была очень теплой."
    heroine "С тобой мне все кажется более значимым."
    $ emotion += 10

    "Они вышли из зала, наслаждаясь моментом."
    $ knowledge += 10
    $ emotion += 10
    jump final_ending

label leave_alone:
    scene school_hall with fade
    play music "audio/bgm_school.ogg" fadein 2.0
    show mc at center
    "Главный герой вышел из зала один, наслаждаясь тишиной."
    mc "Наконец-то я закончил, все кажется сном."
    $ knowledge += 10

    "Главный герой шел по школьным дорожкам, вспоминая прошлое."
    $ knowledge += 10
    jump final_ending

# ========== Финальные концовки ==========
label final_ending:
        if knowledge >= 80 and (programming_skill >= 70 or data_analysis_skill >= 70) and communication_skill >= 60:
            jump elite_ending
        elif creativity >= 80 and knowledge >= 70 and (programming_skill >= 60 or data_analysis_skill >= 60):
            jump pioneer_ending
        elif emotion >= 70 and stress <= 30 and knowledge >= 50:
            jump happy_ending
        elif knowledge <= 40 and stress >= 70 and emotion <= 30:
            jump lost_ending
        elif programming_skill >= 90 and creativity >= 80 and knowledge >= 70:
            jump tech_guru_ending
        elif data_analysis_skill >= 90 and communication_skill >= 70 and knowledge >= 80:
            jump data_expert_ending
        elif emotion >= 90 and knowledge >= 70 and stress <= 20:
            jump happy_couple_ending
        else:
            jump default_ending

# ========== Варианты концовок ==========
label elite_ending:
    scene office with fade
    play music "audio/bgm_ending.ogg" fadein 2.0
    show mc at center
    "Главный герой стал выдающимся специалистом в своей области, достигнув карьерных высот."
    return

label pioneer_ending:
    scene startup_office with fade
    play music "audio/bgm_ending.ogg" fadein 2.0
    show mc at center
    "Главный герой основал свою компанию, став пионером в индустрии."
    return

label happy_ending:
    scene home with fade
    play music "audio/bgm_ending.ogg" fadein 2.0
    show mc at center
    show heroine at right
    "Главный герой нашел баланс между работой и личной жизнью, живя счастливо с героиней."
    return

label lost_ending:
    scene park with fade
    play music "audio/bgm_ending.ogg" fadein 2.0
    show mc at center
    "Главный герой потерялся в жизни, не найдя своего пути."
    return

label tech_guru_ending:
    scene tech_conference with fade
    play music "audio/bgm_ending.ogg" fadein 2.0
    show mc at center
    "Главный герой стал экспертом в технологиях, выступая на международных конференциях."
    return

label data_expert_ending:
    scene book_signing with fade
    play music "audio/bgm_ending.ogg" fadein 2.0
    show mc at center
    "Главный герой стал известным аналитиком данных, опубликовав книгу."
    return

label happy_couple_ending:
    scene home with fade
    play music "audio/bgm_ending.ogg" fadein 2.0
    show mc at center
    show heroine at right
    "Главный герой и героиня построили крепкие отношения, живя счастливо вместе."
    return

label default_ending:
    scene city with fade
    play music "audio/bgm_ending.ogg" fadein 2.0
    show mc at center
    "Главный герой нашел баланс в жизни, живя спокойно и счастливо."
    return