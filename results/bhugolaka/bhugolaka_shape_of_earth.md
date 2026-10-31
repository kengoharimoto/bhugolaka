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
- Not in the corpus: Brahmagupta's Golādhyāya (only the mathematical chapters are present), Lalla's Śiṣyadhīvṛddhida, Pañcasiddhāntikā, Siddhāntaśiromaṇi Golādhyāya. These are the main places for the anti-Jaina and anti-Purāṇic polemics.
- The "cart-shaped / mirror-disc" party in the Āryabhaṭīya commentary is unidentified.
- The *Golādarśa/Goladarpaṇa* Vaṃśīdhara cites is unidentified; it is unclear whether it is his own earlier work.
- Viśvanātha promises the *upapatti* for the 25-koṭi sun "later" (on 5.20.43); 5.21–22 were not OCR'd.
- The Nīlakaṇṭha passage should be checked against his Bhāratabhāvadīpa on the Bhīṣmaparvan in the corpus.
- *Kūrmapṛṣṭha*: the scorched earth at pralaya "like a tortoise's back" (MBh 12.225.2, ViP 6.3.23, Vāyu 2.38.151, BndP 3.1.147, KūrmP 2.43.23) describes a bare surface, not the earth's cosmological shape; left aside.
