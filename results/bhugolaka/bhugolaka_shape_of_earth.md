# Bhūgola(ka) and the shape of the earth

Corpus survey, 2026-10-31 (Mac copy of `E-texts/1_sanskr`).

**Question.** What does *bhūgola(ka)* mean across the corpus, and who held that the earth is a globe? Was it the Jyotiṣa authors?

**Answer.** Yes for Jyotiṣa: from Āryabhaṭa on the earth is explicitly a sphere, and the commentary argues against disc- and cart-shaped earths. The word *bhūgola(ka)* alone proves nothing, though. In the Bhāgavata and the Purāṇas that follow it, *bhū-gola* names the flat Purāṇic disc of dvīpas and oceans. Outside Jyotiṣa the globe is taken up by Mīmāṃsā (Kumārila and the Ajitā), Nyāya-Vaiśeṣika (as the largest earthy whole), the Mokṣopāya/Yogavāsiṣṭha and Kashmir Śaivism (Abhinavagupta, Kṣemarāja).

## Method

- Regex over `1_sanskr/**/*.txt` for `(bhū|kṣiti|mahī|dharā|dharaṇī|pṛthvī|pṛthivī|bhūmi|ku)[-+ ]?gol…` (about 230 hits; hyphenated forms caught in a second pass).
- Proximity searches: *golākāra/golākṛti*, *kadamba-puṣpa/kusuma*, *chatrākāra / kūrmapṛṣṭha / ādarśa-tala / darpaṇodara / samatala* near earth words; *jyotiḥśāstra/jyautiṣa/gaṇaka* near *bhūgola/bhūmaṇḍala/golākāra*.
- Scripts: `../../scripts/kwic.py`, `../../scripts/prox.py` (run from the E-texts root). Raw KWIC dumps in `../../data/`.
- Line numbers are those of the Mac copy of the corpus files.

## 1. Jyotiṣa: an explicit, argued sphere

### Āryabhaṭīya, Golapāda 6–7
`1_sanskr/6_sastra/8_jyot/aryabhata_aryabhatiya.txt:8092`

> vṛttabhapañjaramadhye kakṣyāpariveṣṭitaḥ khamadhyagataḥ |
> mṛjjalaśikhivāyumayo bhūgolaḥ sarvato vṛttaḥ || 6 ||
> yadvat kadambapuṣpagranthiḥ pracitaḥ samantataḥ kusumaiḥ |
> tadvad dhi sarvasattvair jalajaiḥ sthalajaiś ca bhūgolaḥ || 7 ||

Round on every side; covered with beings all over like a kadamba head with its florets.

### Commentary (Shukla ed., INSA 1976)
The e-text merges Bhāskara I and Someśvara. The running commentary is taken here as Bhāskara I's; check against the print.

- **Rejects other shapes** (on Gola 5, `:7850`): *bhuvaṃ tāvad anye śakaṭākārāṃ darpaṇavṛttākārāṃ ca manyante | naitad evam | yathā golākārā bhūḥ pratipadyate tathottarato vakṣyāmi.* Planets look like discs only because they are far away (*dūradeśavartitvād darpaṇavṛttākārā upalakṣyante*).
- **Up and down are relative** (on Kālakriyā 15, `:6745ff.`): *sarveṣām asmadādīnāṃ bhūr adhaḥ, upari cākāśaḥ*, with the kadamba verse quoted in support.
- **Curvature argument** (`:2844`): *iyaṃ ca dharitrī golākārā paṭhyate | tena tatpṛṣṭhavartinām asmākaṃ vakratvāt paridheḥ śaṅkucchāyābhujakoṭikarmaparikalpanā atra na pravartate … na caitāvatyā bhuvaḥ śakyate samīkaraṇaṃ kartum.* The flat shadow-triangle fails on a curved surface of this size.
- **Against Purāṇic geography** (`:887`): rejects the dvīpa-doubling scheme and the Purāṇic Gaṅgādvāra–Kumārī distance of 1000 yojanas against measured distances (Laṅkā–Ujjayinī 200); large Purāṇic yojana-figures are answered *golākāratvād bhuvaḥ | tatpṛṣṭhaparidhyuparicakravyavasthitā ete deśāḥ*.
- **Rotation** (Gola 9, `:8164`): the comment first reads the verse as a rotating earth, then rejects that (*idam asya ādarśanam*: oceans would flood, birds could not return to their nests) and reinterprets it. Not yet settled whether this layer is Bhāskara I's or Someśvara's.

### Sūryasiddhānta 12
`1_sanskr/6_sastra/8_jyot/unknown_suryasiddhanta.txt:1311–1378`

- 12.32: *madhye samantād aṇḍasya bhūgolo vyomni tiṣṭhati | bibhrāṇaḥ paramāṃ śaktiṃ brahmaṇo dhāraṇātmikām.*
- 12.34–35: *bhūgolamadhyago merur ubhayatra vinirgataḥ*. Meru runs through the globe and comes out at both poles: gods above, asuras below. A synthesis with Purāṇic Meru.
- 12.53–54: *sarvatraiva mahīgole svasthānam upari sthitam | manyante khe yato golas tasya kvordhvaṃ kva vādhaḥ || alpakāyatayā lokāḥ svasthānāt sarvatomukham | paśyanti vṛttām apy etāṃ cakrākārāṃ vasundharām.* People see the round earth as a flat disc because they are small. An explicit account of apparent flatness.

### Varāhamihira, Pañcasiddhāntikā 13
Two editions in `1_sanskr/6_sastra/8_jyot/` (added 2026-10-31; uncorrected OCR): `varahamihira_pancasiddhantika_ed-pingree.txt` (Neugebauer–Pingree 1970, PDF pp. 110–111, with Pingree's translation) and `varahamihira_pancasiddhantika_w_sudhakara-dvivedi.txt` (Thibaut–Dvivedi 1889, PDF pp. 90–91). Text as in Pingree, corrected from the OCR:

- **13.1:** *pañcamahābhūtamayas tārāgaṇapañjare mahīgolaḥ | khe 'yaskāntāntaḥstho loha ivāvasthito vṛttaḥ*. The earth-globe of the five elements stands in the cage of stars like a round piece of iron held between lodestones.
- **13.2:** *tarunaganagarārāmasaritsamudrādibhiś citaḥ sarvaḥ | vibudhanilayaḥ sumerus tanmadhye 'dhaḥ sthitā daityāḥ*. Covered all over with trees, mountains, towns and seas; Sumeru, the gods' home, in the middle; the Daityas below.
- **13.3–4:** relativity of up and down. The Asuras appear inverted to the gods like reflections at a water's edge, and they think the gods are below. Fire rises and heavy things fall *asurāṇāṃ tadvad evādhaḥ*.
- **13.6–7:** *bhramati bhramasthiteva kṣitir ity apare vadanti noḍugaṇaḥ | yady evaṃ śyenādyā na khāt punaḥ svanilayam upeyuḥ*. Against Āryabhaṭa's rotating earth: hawks could not return to their nests, and flags would always stream west.
- **13.8:** against the two suns (the Jaina view), from the Dhruva.
- There is no polemic against a flat earth here, only against rotation and two suns. Pingree's apparatus notes that 13.1–4 are quoted by Utpala on Bṛhatsaṃhitā 2, and 13.1 by Pṛthūdaka on BSS 21 and by Nīlakaṇṭha.

### Brahmagupta, Brāhmasphuṭasiddhānta 21 (Golādhyāya)
`1_sanskr/6_sastra/8_jyot/brahmagupta_brahmasphutasiddhanta_w_vasana-vijnana_vol-4.txt` (added 2026-10-31; uncorrected OCR of R. S. Sharma 1966, vol. IV). Ch. 21 is printed twice: with Sudhākara's bhāṣya, the editor's Vijñānabhāṣya and Hindi (PDF pp. 233ff.), and in an appendix with **Pṛthūdakasvāmin's Vāsanābhāṣya** (PDF pp. 520ff.).

- **21.2:** *śaśibudhasitārkakujaguruśanikakṣāveṣṭito bhakakṣāntaḥ | bhūgolaḥ sattvānāṃ śubhāśubhaiḥ karmabhir upāttaḥ*. The bhūgola is wrapped in the planetary orbits inside the star-sphere, acquired by beings through their good and bad karma.
- **21.3:** *khe bhūgolas tadupari merau devāḥ sthitās tale daityāḥ*. The globe is in space, the gods on Meru at the top, the Daityas at the bottom, each with their own pole overhead.
- **21.9:** Avantī lies north of Laṅkā at 1/15 of the earth's circumference.
- **Pṛthūdaka on 21.1** (p. 522) explains why the gola is needed by listing *nirupapattika* (unfounded) doctrines:
  - eclipses caused by Rāhu;
  - *darpaṇodarāyāṃ pṛthivyāṃ samudradvīpāvasthitā parataḥ parato dviguṇaḥ*, a mirror-flat earth with oceans and dvīpas each double the last;
  - a huge square Meru (*mahāpramāṇacaturaśrameru*);
  - the Jina-śāstra's two suns, two moons and 54 nakṣatras.

  He calls all of this *kapolavyāyāmaparāyaṇānām asatprajñāvilasitam*, the bad thinking of people given to exercising their cheeks.
- **Pṛthūdaka on 21.2** (p. 523): what the gola establishes includes *meror mahattvanirākaraṇam* and *bhūgolasya samudraparidher anyo mahān paridhir nāstīti śeṣasamudrāṇāṃ mahattvanirākaraṇam*. Meru is not huge, and no great outer oceans lie beyond the one ocean round the globe.
- **Vijñānabhāṣya (R. S. Sharma) on 21.2** (p. 233) quotes Śrīpati's Siddhāntaśekhara: *ādarśodarasannibhā bhagavatī viśvambharā kīrtitā kaiścit, kaiścana kūrmapṛṣṭhasadṛśī, kaiścit sarojākṛtiḥ | asmākaṃ tu kadambapuṣpanicayagrantheḥ samā sammatā sarvatrāsumatāṃ cayena nicitā toyasthalasthāyinām*. So the competing shapes are mirror-flat, the humped back of a tortoise, and a lotus, against the astronomers' kadamba-ball. He glosses the first as the view of *kecit paurāṇikāḥ*.
- **BSS 11 (Tantraparīkṣā)**, `…_vol-3.txt`:
  - **11.3** (PDF p. 106): *bhāni catuṣpañcāśad dvau dvāv arkendavau jinoktaṃ yat | dhruvamatsyasyāvarto bhavati yato 'hnā tatas tad asat*. The Jaina 54 nakṣatras and two suns and moons are false, because the Dhruvamatsya turns once a day.
  - **11.17** (pp. 134–135): *prāṇeneti kalāṃ bhūr yadi tarhi kuto vrajet kam adhvānam | āvartanam urvyāś cen na patanti samucchrayāḥ kasmāt*. Against Āryabhaṭa: if the earth moves one minute of arc per prāṇa, where would anyone go, and why don't tall things fall? Sudhākara and the Vijñānabhāṣya object that Brahmagupta didn't realise the atmosphere turns with the earth (*bhūvāyusahitāyā bhūmeḥ prāgbhramaṇam*), and that Parameśvara explained Āryabhaṭa's verse away.
  - Ch. 11 also faults Āryabhaṭa's figure for the earth's diameter, but has nothing on its shape.

### Bhāskara I, Mahābhāskarīya 5.4, with Govindasvāmin's Bhāṣya and Parameśvara's Siddhāntadīpikā
`1_sanskr/6_sastra/8_jyot/bhaskara-i_mahabhaskariya_w_govindasvamin-paramesvara.txt` (added 2026-10-31; uncorrected OCR of Kuppanna Sastri 1957; PDF pp. 391–399). The root verse only gives the diameters of sun, moon and earth. **Govindasvāmin** (9th c.) uses it to argue the whole case:
- The planets are spheres (*golākāra*), not mirror-discs (*darpaṇavṛttākāra*), as the moon's phases show. He quotes Ā Gola 5 and 37.
- **The earth:** *kathaṃ punar bhūmes tathākāratā? … kaiścit tāvad anyathākārā mahāpramāṇā ca bhūr abhihitā | dṛśyate ca nimnonnatākāratayā*. Others describe the earth as a different shape and enormous; it also looks uneven; and how could people live on a ball? (Ā Gola 7 quoted.)
- **Answer:** the śāstras disagree (*darśanabhedaḥ*), and the question is settled by *anyathānupapatti* (inference from what could not otherwise be).
  - The pole star stands on the horizon at Laṅkā and at the zenith at Meru, so Meru is a quarter of the circumference from Laṅkā. The yojanas measured between cities by their latitudes confirm Āryabhaṭa's figure, *na paurāṇikadṛṣṭiyuktāni*: not the figures of the Purāṇic view.
  - *mahocchrāyapramāṇameruparikalpanāpi na ghaṭate*: a huge Meru would hide the stars that are seen rising north of the pole.
  - The earth's unevenness comes from the deposits that build up on it (Ā Gola 8).
  - Everyone's "down" is the earth (Ā Gola 12, 20).
- **Against falling:** thrown clods come back down.
- **Against rotation:** the oceans would flood the land, mountains would be thrown off, birds could not regain their nests.
- **Against Śeṣa and the like as support:** infinite regress. The earth stays up *svaśaktyaiva*.
- Āryabhaṭa's number of eastward revolutions of the earth (*ku-ṅiśivuṇḷṣkhṛ prāk*) is reread as the star-wheel's motion attributed to the earth by an illusion (*mithyājñāna*), as stationary things seem to move to someone in a boat.
- Parameśvara's Siddhāntadīpikā glosses all of this without dissent.

### Vaṭeśvara, Gola 5 (Bhūgola)
`1_sanskr/6_sastra/8_jyot/vatesvara_vatesvarasiddhanta_w_gola.txt` (added 2026-10-31; uncorrected OCR of Shukla's INSA ed.; PDF pp. 348–350). Shukla's footnotes match most verses to Lalla's Gola.
- **1:** *karmabhir mṛdubhujāṃ śubhāśubhair vyomavāyuśikhitoyamṛṇmayaḥ | bhagrahaiḥ supariveṣṭito 'mbare nirmitas tv avanigolako 'calaḥ*.
- **2:** the iron ball between lodestones (cf. Pañcasiddhāntikā 13.1).
- **3, 7:** there is no "down" for the globe to fall to.
- **5–6:** against Śeṣa, the tortoise, the mountains and the elephants as support.
- **8:** the house-lizard on a hanging pot.
- **10–12:** the four cities, gods and Daityas, and the kadamba simile.

### Āryabhaṭa II, Mahāsiddhānta 16 (Bhuvanakośa)
`1_sanskr/6_sastra/8_jyot/aryabhata-ii_mahasiddhanta_w_sudhakara-dvivedi.txt` (added 2026-10-31; uncorrected OCR of Dvivedin 1910; PDF pp. 240–247).
- **4:** *vasudhā nānyādhārā tiṣṭhati gagane svaśaktyaiva*. Sudhākara notes that this author does not follow the "elder Āryabhaṭa", for whom the earth turns.
- **5:** *kandukarūpā dhātrī sarvatrāmbhodhiparvatadvīpaiḥ*. The earth is shaped like a ball, with oceans, mountains and dvīpas all round; the pātālas are its hollows.
- **6–8:** gods, Daityas and humans walk on the ball as we do. Laṅkā is "on top" only by convention.
- **9–29:** the Purāṇic geography is mapped onto the globe: Jambūdvīpa as the northern half beyond the salt ocean, the other dvīpas and oceans, the varṣas and their mountains, Meru with Mandara and the rest. This is the clearest attempt in the corpus to put the Purāṇic map on a sphere.
- **36:** a 110th part of the circumference is flat, *ataḥ sameva bhūr bhāti*.

### Parameśvara, Golādīpikā
`1_sanskr/6_sastra/8_jyot/paramesvara_goladipika.txt` (added 2026-10-31; uncorrected OCR of TSS 49, poor scan; PDF pp. 8–10).
- **22–23:** the sun and moon are spheres. *darpaṇavṛttākāraṃ maṇḍalam icchanti ye tu te mugdhāḥ*: those who take them for discs are fools, as the moon's phases show.
- **After 23:** *golākārā pṛthivī khe tiṣṭhati sarvadā svaśaktyaiva*. Land lies in the upper half, water in the lower.
- **Supports and rotation:** *bhūmir anantena dhṛtety eke 'nye diggajair iti bruvate* is rejected by regress. *pūrvābhimukhaṃ bhramati kṣoṇī … iti kila vadanti kecit nābhimataṃ tad api cāryabhaṭasya*: rotation is said not to be Āryabhaṭa's own view.
- **Size:** *bhūmer yojanamānaṃ bahukoṭimitaṃ vadanti sudhiyo 'nye | naitad gaṇakābhimataṃ*. A size of many crores of yojanas is rejected, since latitude differences give the real size.
- **v. 33 and the next verse:** a reconciliation (*vākyāvirodha evaṃ vicintya sudhiyā sudhībhir iha neyaḥ*) that treats the large Purāṇic figures as measures over the whole globe and its inner pātālas. The OCR is poor here and this reading is tentative.
- **Meru:** *atyunnatiś ca meror na cintyate golavidbhiḥ*. Meru's great height is not accepted, because stars rise north of the pole. This is Govindasvāmin's argument.

### Lalla, Śiṣyadhīvṛddhida (Gola)
`1_sanskr/6_sastra/8_jyot/lalla_sisyadhivrddhida_w_mallikarjuna.txt` (added 2026-10-31; uncorrected OCR of Chatterjee 1981; verse numbers as in her edition; PDF pages of the scan).

- **Bhuvanakośa (adhikāra 17), vv. 5–8** (PDF pp. 237–238):
  - Up and down are relative: *sarveṣām upari nabhas tadadho bhūr upari te bhūmeḥ* (5).
  - The kadamba image again: *tarunaganagarasurāsuranarair ayaṃ kesarair iva samantāt | golaḥ kādambo madhukarībhir iva sarvataḥ pracitaḥ* (6).
  - People on the underside are like a house-lizard running along the beams of a ceiling (*yathā gṛhagodhikā*, 7).
  - Fire rises and heavy things fall toward the ground, *na talam asti bhuvaḥ kva patatv asau*: the earth has no ground to fall to (8).
- **Mithyājñānādhyāya (adhikāra 20)**, a whole chapter refuting wrong views (PDF pp. 256–263).
  - v. 6 lists the views about the earth: *amitām avanīṃ pracakṣate susamāṃ kecana darpaṇopamām | apare bahuyojanām imāṃ salilasthām atha yānapātravat*. Some say it is boundless, or perfectly flat like a mirror; others that it is many yojanas wide, or floats on water like a ship.
  - vv. 30–33: a boundless or vast earth contradicts observation; Avanti lies 1/16 of the circumference from Laṅkā.
  - **vv. 34–37 refute the flat earth:** *yadi darpaṇavat samā mahī* (34). On a mirror-flat earth, why would rain fall instead of running off sideways? A hundredth of the circumference looks straight (35). On a flat earth, tall trees far away would never sink out of sight (36). The earth only looks *susamā darpaṇavat* because the sky seems to meet it all round at the horizon (37).
  - v. 38: against the earth's falling. vv. 39–41: against its resting on water, or on a tortoise or the like (*kamaṭhādibhir uddhṛtā mahī … kena dhṛtāḥ?*).
  - **vv. 42–43 against rotation:** birds could not find their nests, arrows would land toward the ocean, clouds would drift west.
  - v. 44: against two suns and moons (the Jaina view).

### Bhāskara II, Siddhāntaśiromaṇi, Golādhyāya, Bhuvanakośa
`1_sanskr/6_sastra/8_jyot/bhaskara_siddhantasiromani_goladhyaya_w_vasana-marici_pt-1.txt` (added 2026-10-31; uncorrected OCR of the Ānandāśrama ed. with Bhāskara's Vāsanā and Munīśvara's Marīci; PDF pages of the scan).

- **vv. 2–3** (p. 33): *bhūmeḥ piṇḍaḥ śaśāṅkajñakaviravikujejyārkinakṣatrakakṣāvṛttair vṛto vṛtaḥ san mṛdanilasalilavyomatejomayo 'yam | nānyādhāraḥ svaśaktyaiva viyati niyataṃ tiṣṭhati …*, and again *kadambakusumagranthiḥ kesaraprasarair iva*. The Vāsanā glosses *vṛtto vartulākāraḥ*.
- **vv. 5–6** (p. 37): the earth's own power holds it, as heat belongs to fire. **Attraction:** *ākṛṣṭiśaktiś ca mahī tayā yat khasthaṃ guru svābhimukhaṃ svaśaktyā | ākṛṣyate tat patatīva bhāti same samantāt kva patatv iyaṃ khe*. The Marīci adds Sūryasiddhānta 12.32.
- **vv. 7–10** (pp. 43–46): the Bauddhas say the unsupported earth falls forever, unnoticed, as someone in a moving boat does not notice the boat moving. The Jainas posit two suns, two moons and double nakṣatras around a pillar-like Meru. Bhāskara answers the Jainas with the turning of the Dhruvamatsya (10).
- **vv. 11–12** (p. 47): against the flat earth: *yadi samā mukurodarasannibhā bhagavatī dharaṇī …*. If the earth were flat, people would see the sun at all times, as the gods do. If Meru caused night, Meru would be visible, and the sun would always rise in the north. The Vāsanā names the opponent: *purāṇe bhūḥ samādarśodarasannibhā kathyate | tanmadhye meruḥ …* and summarises the dvīpa scheme. Munīśvara's Marīci quotes the Bhāgavata itself as the Purāṇic view (BhP 5.16.5 *samavartulo yathā puṣkarapatram*; 5.20.35 *kāñcany anyādarśatalopamā*) and refutes it from the varying length of day and night.
- **v. 13** (p. 52): why the earth looks flat: *samo yataḥ syāt paridheḥ śatāṃśaḥ pṛthvī ca pṛthvī nitarāṃ tanīyān | naraś ca tatpṛṣṭhagatasya kṛtsnā sameva tasya pratibhāty ataḥ sā*. A hundredth of a circumference is flat to the eye, the earth is very large and man very small. The Marīci quotes Sūryasiddhānta 12.54 (*alpakāyatayā lokāḥ … cakrākārāṃ vasundharām*).

The sequence:
- **Varāhamihira (6th c.)** argues only against rotation and two suns.
- **Brahmagupta (628)** argues against rotation and the Jaina two suns (BSS 11), but not against a flat earth.
- **Lalla (8th c.?)** refutes a mirror-flat earth at length but leaves it anonymous (*kecana*).
- **Govindasvāmin (9th c.)** argues that the earth is a sphere against "others" who make it "a different shape and enormous". He sets the measured size against the Purāṇic figures and the visible stars against a huge Meru.
- **Pṛthūdaka (9th c.)** already rejects a mirror-flat earth with doubling dvīpas and oceans, the Purāṇic scheme, alongside the Jaina doctrines, but names no source.
- **Āryabhaṭa II** instead lays the Purāṇic dvīpas and Meru onto the ball.
- **Śrīpati (11th c.)** sets three non-astronomical shapes against the astronomers' kadamba-ball.
- **Bhāskara II (12th c.)** names the Purāṇa as the source of the flat earth.
- **Parameśvara (15th c.)** rejects a size of crores of yojanas and a towering Meru, but looks for a way to make the statements agree.
- **Munīśvara (17th c.)** quotes the Bhāgavata's own words.

## 2. Purāṇic *bhūgola*: the disc

- **Bhāgavata 5.16.4** introduces the cosmography as *bhū-golaka-viśeṣaṃ nāma-rūpa-māna-lakṣaṇato vyākhyāsyāmaḥ*. What follows is flat:
  - 5.16.5: Jambūdvīpa *samavartulo yathā puṣkara-patram* (round like a lotus leaf);
  - 5.16.7: Meru the pericarp (*karṇikā*) of the earth-lotus;
  - 5.20.35: the golden land beyond, *ādarśa-talopamā*;
  - 5.20.38: Lokāloka is a quarter *pañcāśat-koṭi-gaṇitasya bhū-golasya*;
  - 5.25.12: Śeṣa bears the *bhū-gola* on one head like an atom.
- **Devībhāgavata** copies it: *karṇikārūpa evāyaṃ bhūgolakamalasya ca* (`1_sanskr/3_purana/unknown_devibhagavatapurana.txt:27377`); *bhūgolasya caturthāṃśo lokālokācalaḥ*.
- **Nṛsiṃhapurāṇa 30** (*bhūgolakathana*: *ataḥ paraṃ pravakṣyāmi bhūgolaṃ*, then the seven dvīpas) and **Nāradapurāṇa 1.3** colophon use *bhūgola* as the label for dvīpa cosmography. Jīva Gosvāmin (Bhagavatsandarbha) calls BhP 5.16 the *bhūgola-praśna*.
- *Bhūgola* does not occur in Viṣṇu, Vāyu or Matsya in this corpus. Inference, not verified: the Bhāgavata took a Jyotiṣa term for its own disc.
- **Partial absorption of Jyotiṣa:** Vahnipurāṇa (`1_sanskr/3_purana/unknown_vahnipurana.txt:2059`): night is the shadow cast by the *sumeru-bhūgolaka*; eclipse by *golakacchāyā*.
- **Kāvya mixes the images:** Mālatīmādhava 5.22 *namad-bhūgola-niṣpīḍana-nyañcat-karpara-kūrma…*; commentators gloss *bhūmipiṇḍa*, *avanicakra* (Jagaddhara), *bhuvaḥ saṃsthānam*. Gītagovinda 1.16, Varāha *bhūgolam udbibhrate*.

## 3. The globe outside Jyotiṣa

### Mīmāṃsā
- **Kumārila, Tantravārttika** on *uttānā vai devagavā vahanti* (`1_sanskr/6_sastra/3_phil/mimamsa/kumarila_tantravarttika.txt:5677`): *atha vā bhūmiṣṭhānām eva satāṃ kenāpi guṇavādena pṛthivīgolaka-trailokya-bhramaṇādinā vā purāṇoktena dṛṣṭivaśād yathaiva vayam upari devān paśyāma evam adho dyuparivartanād ayam api loko devair upari dṛśyata iti uttānavahanadṛṣṭiḥ.* He ascribes the earth-globe to *purāṇa*.
- **Ajitā on the passage** (file `1_sanskr/4_rellit/saiva/agama/unknown_ajita_adhyaya-1_iast.txt:12799`, which is the TV with the Ajitā): *anenaitat siddhyati nordhvādhobhāvo niyataḥ kintu ya eva yasyādhāraḥ tad eva tasyādho viparītam ūrdhvam iti*; otherwise people would sometimes find themselves hanging head-down.
- **Śabara on MS 6.7.3** (`jaimini_mimamsasutra_w_sabarabhasya_adhyayas_1-7.txt:15348`): *yad etan mṛdārabdhaṃ dravyāntaraṃ pṛthivīgolakam, na kṣetramātraṃ*. The whole earth as one substance; says nothing about shape. Also Śālikanātha, Pañcikā: *bhūgolakaṃ gopatharājamārgajalādisamanvitam*.

### Nyāya-Vaiśeṣika: the largest earthy whole
- Udayana, Kiraṇāvalī: *kintv ā paramāṇor ā ca bhūgolakāt pṛthivītvanimittākrānte …* (`udayana_kiranavali_dravya.txt:173`).
- Śrīdhara, Nyāyakandalī: darkness as substance would show its parts *mahāndhakāre ca bhūgolakasyeva* (`sridhara_nyayakandali_jetly-ed.txt:130`); *bhūpradeśāḥ bhūgolakalpapradeśāḥ*; *mahābhūtānāṃ bhūgolakādīnāṃ ca prakṣobhaṇaṃ calanam* ascribed to adṛṣṭa. The darkness argument is reused in the Jaina Dravyālaṅkāra.
- Gaṅgeśa, TC Śabda: *bhūgolakasantāno 'yaṃ bhūgolakasantānānadhikaraṇavṛttidhvaṃsapratiyogī kāryatvāt*; Vyāsatīrtha, Tarkatāṇḍava: *dvyaṇukādibhūgolakaparyanta*; Jayatīrtha, Nyāyasudhā.
- Bhaṭṭoji, Prauḍhamanoramā (`1_sanskr/6_sastra/1_gram/bhattoji-diksita_praudhamanorama.txt:2034`) faults Udayana's *ā ca bhūgolakam* as *prāmādika*; read *ā bhūgolakāt*. Repeated in the Tattvabodhinī.

### Mokṣopāya / Yogavāsiṣṭha
- **Mokṣopāya 1.25.34** (`1_sanskr/6_sastra/3_phil/vedanta/unknown_moksopaya.txt:6557`): *dharāgolakam antaḥsthasurāsuragaṇāspadam | veṣṭyate dhiṣṇyacakreṇa pakvākṣoṭam iva tvacā*; Bhāskarakaṇṭha glosses *bhūgolam*.
- **YV Nirvāṇa-u. 127, *bhūgolanirṇaya*** (`1_sanskr/6_sastra/3_phil/yogavasistha/unknown_yogavasistha_khanda-2_org.txt:69539–69715`): Rāma asks *kathaṃ bhūgolakaṃ sthitam*; Vasiṣṭha compares it to a ball (*vīṭā*) a child imagines in the sky. Ānandabodhendra (Tātparyaprakāśa) on v. 8 lists the *vādins*' views:
  1. The earth falls forever through endless space; we don't notice because it is so large, and the star-wheel, tied to the two poles on Meru, falls with it and spins.
  2. It floats on an ocean like a boat (*yo 'psu nāvaṃ pratiṣṭhitāṃ veda*), sinks at pralaya, rises at creation like a gourd.
  3. Infinite water all round; the wind in its seven hollow worlds keeps it rising like a submerged gourd.
  4. Only space all round; it always falls south, south being "down" from the gods' view on Meru.
  5. The *āsura* view: pātāla is up, so it falls north. People in east and west likewise each take their own side as up.
  6. The star-wheel does not turn; the earth turns in place, and we see the stars move as people in a boat see the trees move.
  7. The earth is "down" from every side for those standing around it; with no fixed down there is no direction to fall, so it stays where it is.
  Vasiṣṭha's own answer: each is true for the consciousness that imagines it.
- **YV Nirvāṇa-u. 131.7–17:** *kanduke vyomni saṃruddhe daśadikkaṃ pipīlikāḥ | itthaṃ bhramanti bhūtāni*; the princes who set out to find the end of the earth keep circling, *deśaṃ bhūgolakasyāsya yaṃ yam āsādayanti ca | iheva tatra tatroccair adhaś cordhvaṃ*.
- **YV Nirvāṇa-u. 205.14:** antipodal peoples, *budhnākāśād ūrdhvakhurā lambamānavanācalāḥ*.
- **YV Utpatti 30.12** (`unknown_yogavasistha_utpattiprakarana.txt:9727`): *pipīlikānāṃ mahatāṃ vyomni vartulaloṣṭake | daśadikkam adhaḥ pādāḥ*; comm.: *bhūgolaṃ sarvataḥ khagolena … veṣṭitam ity abhyupagacchatāṃ jyotiḥśāstrakṛtām api saṃmataḥ*. Also Utpatti 24.63, lunar eclipse explained by the earth's shadow (*jyautiṣikaprakriyām āśritya*).

### Kashmir Śaivism
- **Abhinavagupta, ĪPVV** (`1_sanskr/4_rellit/saiva/trika/abhinavagupta_isvarapratyabhijnavivrtivimarsini_vol-3_m00022.txt:2412`): the over-proud reasoner is *svagṛhaprāṅgaṇamadhyakalpitaniḥśeṣabhūgolakamadhyadhruvakasthānavan mūḍhaḥ*. He puts the pole star over the centre of the whole earth-globe as he imagines it from his own courtyard. This seems to show awareness that the pole's position depends on latitude.
- **Kṣemarāja, Uddyota on Svacchanda 10.511** (`1_sanskr/4_rellit/saiva/unknown_svacchandatantra_w_ksemaraja-uddyota_m00091.txt:16378`): what Jyotiṣa says of the star-wheel *bahirbhūgolam* and the positions and sizes of sun, earth and the rest holds for its own purpose, reading karma (quotes Laghujātaka 1.3 *yad upacitam anyajanmani …*), relative to the luminaries as *tejogolaka*s. The Āgama's account is the real one (*vāstavam*), so *na tena saha saṃvādavisaṃvādādicarcā kāryā*. Also on 10.323: *madhyama iti bhūgolāpekṣayā*.

## 4. The Bhāgavata commentators on 5.16–20

Added 2026-10-31. No commentary on Skandha 5 is in the corpus, so the source is *Śrīmadbhāgavatam … anekavyākhyāsamalaṅkṛtam*, Skandha 5, ed. Kṛṣṇaśaṅkara Śāstrī (Ahmedabad 1965), scan at archive.org `SrimadBhagavatamCanto05withMultipleSanskritCommentaries`. PDF pp. 318–474 were OCR'd with Google Vision (archive.org's own OCR is unusable) and transliterated with `sanscript`. Text in `../../data/bhp5_16-20_commentaries_ks1965_vision_{deva,iast}.txt`, page-tagged `=== PDFPAGE n ===`; KWIC in `../../data/kwic_bhp5_commentaries.txt`. Page numbers below are PDF pages; printed page = PDF page − 2.

Commentaries printed on these chapters: Śrīdhara (Bhāvārthadīpikā), Vaṃśīdhara (Bhāvārthadīpikāprakāśa), Vīrarāghava (Bhāgavatacandrikā), Vijayadhvaja (Padaratnāvalī), Jīva (Kramasandarbha), Viśvanātha (Sārārthadarśinī), Śukadeva (Siddhāntapradīpa), Giridhara (Bālaprabodhinī), Bhagavatprasāda (Bhaktamanorañjanī). The Dīpinī, Subodhinī and Subodhinīprakāśa advertised for the volume do not appear on these chapters.

### Most take *bhūgola* as the disc and do arithmetic
- Śrīdhara, Vīrarāghava, Śukadeva, Giridhara and Bhagavatprasāda gloss *bhūgola* as the 50-koṭi-yojana *bhūmaṇḍala* and compute the belts. None of them raises Jyotiṣa.
- On 5.16.5 *samavartulaḥ* is glossed *samo vartulaś ca, vartulatvena koṇābhāvāt sarvataḥ samaparimāṇaḥ* (Vīrarāghava p. 331; Bhagavatprasāda p. 335). Round means a circle without corners.
- Vīrarāghava on 20.41ff. (p. 468) cuts the 50-koṭi *bhūmaṇḍala* from Meru into four triangular sectors, *alpamūlā vipulāgrabhāgās trikoṇākārāḥ*.

### *Gola* as the egg-shell, not the earth
- **Vijayadhvaja** on 20.38 (p. 464): *pañcāśatkoṭivistārayojanātmakasya bhūgolakasya brahmāṇḍalakṣaṇasya*. The bhūgolaka is the brahmāṇḍa.
- **Viśvanātha** on 20.38 (p. 464): *bhūgolakasya bhūsambandhāṇḍagolakasyety arthaḥ | sūryasyeva bhuvo 'py aṇḍagolakayor madhyavartitvāt khagolam iva bhūgolam api pañcāśatkoṭiyojanapramāṇam.* The *gola* is the egg-sphere round the earth. The earth itself is 34 lakh short of 50 koṭi, which leaves 17 lakh yojanas of clearance on every side, so that Śeṣa's bearing it, the dig-gajas steadying it, its sinking in the Cākṣuṣa manvantara and Varāha's lifting it all make sense (*anyathā … aṇḍagolakalagnatve tat tat sarvam akiṃcitkaraṃ syāt*).

### Harmonising Purāṇic accounts, not Jyotiṣa
- **Vijayadhvaja** on 16.7 (p. 332): against the Viṣṇupurāṇa's (Parāśara's) Meru height of 84,000 yojanas, the Bhāgavata wins. He argues that Parāśara can err (*paśyanto 'pi na jānanti meror rūpaṃ vipaścitaḥ*; Indra calls Meru round, Bṛhaspati five-cornered) and cites: *yathā bhāgavate tūktaṃ bhauvanaṃ kośalakṣaṇam | tasyāvirodhato yojyaṃ sarvagranthāntarasthitam …*
- **Jīva**, Kramasandarbha on 16.6–29 (p. 332): *ṭīkādarśitā matabhedāḥ sṛṣṭibhedena jñeyāḥ*. The disagreements the commentators show come from different creations.
- **Jyotiṣa appears only as a calendar term** on 5.17.1 (pp. 350–351): Vaṃśīdhara and Jīva take *yuga* as the 5-year Jyotiṣa yuga, Vaṃśīdhara quoting Śrīpati, *yugaṃ bhaved vatsarapañcakena*.

### Vaṃśīdhara on 5.20.38: the one real engagement (pp. 460–462)
He first reproduces Viśvanātha's egg-sphere reading. He then sets out three ways of reconciling the Purāṇa with Jyotiṣa.

1. **Nīlakaṇṭha on the Mahābhārata, Bhīṣmaparvan**, quoted: *atreyaṃ śāstrānubhavayor avirodhena bhūkalpanā pratibhāti.*
   - The earth is a square with sides of 4650 yojanas. Its diagonal is worked out *śulvaśāstroktarītyā*, with the corners at the sea-junctions; the southern one is Rāmasetu.
   - The jyotirvids' circumference of 4967 yojanas (*saptāṅgacandrābdhi*) roughly corresponds to this. The difference of 317 is put down to different *hasta* standards.
   - The sun circles the tall Meru, so *na bauddhābhimataṃ sūryadvayaṃ kalpyam*. Nīlakaṇṭha also says *anyat sarvaṃ yuktyaviruddhaṃ jyotirvinmatam evātrānusartavyam*.
   - The Purāṇa's 50-koṭi bhūgola is either *acintya* (*acintyāḥ khalu ye bhāvā na tāṃs tarkeṇa sādhayet*) or to be scaled down by 1/20. On that scale Bhāratavarṣa becomes a triangle, which fits *pṛthivī trikoṇeti lokapravādaḥ* and the prime meridian (*purī rakṣasāṃ … kurukṣetram eṣā bhuvo madhyarekhā*).
2. **His own: yojanas of different sizes.** The *hasta* varies (child, adult; Kātyāyana's alternatives), so *jyotiḥśāstrapurāṇetihāsānāṃ virodho yathākathaṃcit parihṛtaḥ syāt*. Neither side overrides the other: Jyotiṣa is *vedacakṣus*, and Vyāsa is Nārāyaṇa. Vyāsa only seems to contradict Jyotiṣa, *asurajanakartṛkaśāstrapravṛttisaṃkocārthaṃ*, to curb a śāstra authored by an asura (presumably Maya's Sūryasiddhānta). Otherwise Vyāsa would be blind to the Veda.
3. **The *Golādarśa* solution** (*asya samādhir golādarśe vihitaḥ*; later *goladarpaṇe*). Its question is why the Bhāgavata's Jambūdvīpa is 1 lakh yojanas when Jyotiṣa's whole earth is 5000.
   - **Two earths:** *pṛthivyā ākāradvayam asti — eko mahāparimāṇako viśeṣākāraḥ, dvitīyo jyotiḥśāstroktaḥ svalpaparimāṇako golākāra eva.*
   - **BhP 5.16.4 names both:** *bhūgolakapadena jyotiḥśāstrokto golākāro mārttiko 'ṇḍaḥ | viśeṣapadena maṇḍalākāraḥ purāṇokto hiraṇmayo 'ṇḍaḥ*. Support is drawn from *tato viśeṣaṃ pratipadya* (Skandha 2) and *etad aṇḍaṃ viśeṣākhyam* (Skandha 3).
   - **Proof that the Bhāgavata itself knows the globe:** Śeṣa holds the earth *siddhārtha iva* (5.25.12, a mustard seed, hence round); *prekṣayitvā bhuvo golam* (Kardama's tour, Skandha 3); *sādridvīpābdhibhūgolam* (10.8.37).
   - **Where the big earth is:** above the nakṣatra-kakṣā, as a magnified reflection (*pratibimbarūpā*). A fire-sphere or water-sphere of 5000 yojanas works *dūrakāntavat* (apparently a telescope), making the small look large. He cites the Puliśasiddhānta, *bhūvātodvayor yoge jalagolo 'sti kācavat*, and Sūryasiddhānta, *atyāsannatayā tena grīṣme tīvrāḥ karā raveḥ*. The 25-koṭi sun of 5.20.43 is the reflected sun, and 5.21.1–2 is reread on this model (*etena bhūgolakendreṇa …*).
   - He ends: *etadvirodhaparihāro yaḥ pūrvam eva mayālekhi sa eva samīcīnaḥ pratibhāti*. He prefers his own earlier solution.

So among the commentators on 5.16–20, only Vaṃśīdhara confronts the Jyotiṣa sphere. Both the solution he reports and Nīlakaṇṭha's keep the small Jyotiṣa earth and put the Purāṇic numbers in a separate register.

## Gaps
- All the Jyotiṣa texts added on 2026-10-31 have now been read for this question (§1). The Tantrasaṅgraha (with Śaṅkara Vāriyar) has nothing on the earth's shape. All of these files are uncorrected OCR. Quotations here are corrected by eye, and the Golādīpikā reconciliation (v. 33f.) is the least certain reading.
- The Śrīpati verse is quoted secondhand from Sharma's Vijñānabhāṣya; the Siddhāntaśekhara itself is not in the library.
- The "cart-shaped / mirror-disc" party in the Āryabhaṭīya commentary is unidentified.
- The *Golādarśa/Goladarpaṇa* Vaṃśīdhara cites is unidentified; it is unclear whether it is his own earlier work.
- Viśvanātha promises the *upapatti* for the 25-koṭi sun "later" (on 5.20.43); 5.21–22 were not OCR'd.
- The Nīlakaṇṭha passage should be checked against his Bhāratabhāvadīpa on the Bhīṣmaparvan in the corpus.
- *Kūrmapṛṣṭha*: the scorched earth at pralaya "like a tortoise's back" (MBh 12.225.2, ViP 6.3.23, Vāyu 2.38.151, BndP 3.1.147, KūrmP 2.43.23) describes a bare surface, not the earth's cosmological shape; left aside.
