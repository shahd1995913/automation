from automation import __version__
from automation.automation.automation import arr_email,arr_phone

def test_version():
    assert __version__ == '0.1.0'

def test_phone_len():
    real=len(arr_phone)
    expected =93
    assert real==expected

def test_str_phone():
    real=str(arr_phone)
    expected = ['008-445-7591', '026-957-0947', '027-008-1146', '031-153-2587', '048-736-2919', '050-322-9622', '057-270-7914', '068-591-1637', '069-491-3390', '085-890-4818', '087-265-5897', '087-879-4133', '100-910-1391', '112-074-4513', '112-565-3516', '127-650-4539', '132-563-4822', '176-099-6255', '178-383-0937', '187-196-7510', '187-338-2109', '221-974-3509', '228-907-6760', '269-857-1421', '303-594-8630', '309-863-9370', '311-994-0963', '313-495-0413', '314-173-1330', '321-717-5991', '322-077-5006', '324-983-5471', '326-697-2146', '333-876-6217', '345-940-6471', '348-559-0354', '355-752-3413', '358-754-0508', '370-935-3291', '385-390-7299', '390-176-8487', '395-258-5024', '408-119-5012', '410-924-4158', '414-851-4313', '415-879-4210', '430-040-4181', '437-807-8509', '443-538-6520', '453-398-5435', '461-108-5810', '461-731-3087', '463-704-8488', '481-468-0721', '489-319-6885', '502-887-8102', '509-234-5018', '521-410-1195', '549-491-0258', '552-403-5262', '557-968-4804', '575-358-8600', '595-877-5199', '604-845-8788', '608-527-5602', '629-334-6313', '653-384-7916', '659-184-4044', '675-699-3626', '678-520-5887', '692-465-5279', '693-728-3320', '708-179-6223', '711-685-3934', '739-004-7296', '751-899-0507', '808-164-5483', '809-031-1744', '822-773-2085', '823-682-3235', '830-478-6024', '862-407-3585', '864-565-6951', '896-573-1016', '903-937-1849', '912-659-6834', '912-930-6083', '916-191-9914', '927-030-2240', '939-181-8494', '946-797-6575', '954-481-4482', '964-915-8108']
    assert real==expected


def test_email_len():
    real=len(arr_email)
    expected =100
    assert real==expected

def test_str_email():
    real=str(arr_email)
    expected = ['aaron84@gmail.com', 'aguilarjoseph@hinton-hardin.org', 'ajohnson@frazier.com', 'amanda61@yahoo.com', 'amberpowell@brown-lewis.com', 'andrea10@yahoo.com', 'ayerschristopher@gmail.com', 'bakerpreston@peters.com', 'bbond@hotmail.com', 'brooksbrian@yahoo.com', 'castrodavid@gmail.com', 'cathylopez@nguyen-hutchinson.com', 'christopherward@gmail.com', 'codymorrow@hotmail.com', 'craiggeorge@myers-lopez.com', 'danielletaylor@hotmail.com', 'davismichele@wright.info', 'deleonchristopher@christian-wilson.com', 'dflores@yahoo.com', 'diane95@alexander.biz', 'djimenez@hotmail.com', 'dodsonjohn@doyle.com', 'earlharvey@gmail.com', 'erin28@gmail.com', 'felicia33@yahoo.com', 'frobbins@stevens.com', 'frodriguez@peters.info', 'garciagabrielle@hotmail.com', 'george55@navarro-price.org', 'gflores@hotmail.com', 'gloria07@gmail.com', 'gnorton@gmail.com', 'hcarter@hotmail.com', 'hendersonjeremy@payne.net', 'herreraelaine@wilson.biz', 'hoffmankarla@mcdonald.com', 'hsoto@sharp-king.com', 'hutchinsonsarah@yahoo.com', 'isaiahthomas@wang.org', 'james06@mann.com', 'james18@lopez.com', 'james19@yahoo.com', 'jeffrey13@gmail.com', 'jgaines@bond.com', 'john34@yahoo.com', 'joneslindsay@figueroa.info', 'josephwolfe@hotmail.com', 'keithperry@white-flores.com', 'kelliboone@yahoo.com', 'kenneth39@gmail.com', 'kevinturner@hotmail.com', 'lacey37@yahoo.com', 'lawrence89@haney.com', 'leeharold@williams.info', 'leeshelley@lowery.com', 'lisajensen@gmail.com', 'lnelson@obrien.com', 'lpitts@hotmail.com', 'martingary@yahoo.com', 'megan54@kramer-solis.com', 'melissa55@hotmail.com', 'melissa67@hotmail.com', 'michaelbutler@gmail.com', 'michaelmoore@scott-wong.net', 'millerjoshua@yahoo.com', 'moorestuart@gmail.com', 'msnyder@holland.com', 'mullinsnicole@simpson.com', 'murphykelly@matthews.com', 'nhill@dominguez.com', 'nicholas74@yahoo.com', 'nicholstracy@jimenez.info', 'ortizjessica@gmail.com', 'patrickkimberly@smith-guzman.org', 'pattersonbradley@hotmail.com', 'petersenbrandon@sweeney-oconnor.com', 'portermiguel@hotmail.com', 'rebeccagreene@cooper.info', 'rebeccaholder@hotmail.com', 'rebeccathomas@ortiz.net', 'renee49@campbell.biz', 'rmeyer@wallace.com', 'robert00@weaver-jefferson.com', 'robin52@smith.biz', 'samuelweber@gmail.com', 'sarah95@cobb-mcfarland.com', 'shannon27@yahoo.com', 'smithrobert@yahoo.com', 'stantonlisa@yahoo.com', 'tcastro@curtis.com', 'thompsonjoshua@gmail.com', 'ugraham@stanley.com', 'upeterson@moreno-roberts.com', 'veronicabarker@yahoo.com', 'vshah@gmail.com', 'waltersmegan@franco.com', 'williamclark@yahoo.com', 'williamsalex@yahoo.com', 'wmiller@gmail.com', 'xharris@lowe.biz']   assert real==expected
    assert real==expected



