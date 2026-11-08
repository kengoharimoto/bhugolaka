# Bhūgola(ka) and the shape of the earth

**Question.** What does *bhūgola(ka)* mean across the Sanskrit corpus, and who held that the earth is a globe? Was it
the Jyotiṣa authors?

**Answer in brief.** Yes for Jyotiṣa. From Āryabhaṭa on, the earth is explicitly a sphere, and the commentators argue
against flat, cart-shaped and mirror-disc earths. The word *bhūgola(ka)* proves nothing by itself, though: in the
Bhāgavata and the Purāṇas that follow it, *bhū-gola* names the flat Purāṇic disc of dvīpas and oceans. Outside Jyotiṣa
the globe is taken up by Mīmāṃsā (Kumārila and the Ajitā), Nyāya-Vaiśeṣika (as the largest earthy whole), the
Mokṣopāya/Yogavāsiṣṭha and Kashmir Śaivism (Abhinavagupta, Kṣemarāja).

**Start here:** `results/bhugolaka/bhugolaka_shape_of_earth.md` (the report). `results/bhugolaka/bhugolaka.html` is the
same report as a page and is kept in step with it.

**Public repository:** https://github.com/kengoharimoto/bhugolaka. It leaves out the OCR of the 1965 Ahmedabad
edition and the KWIC dump taken from it (the edition may still be in copyright); the report cites that edition by PDF
page, and the scan is on archive.org. Licence: CC BY 4.0 for the report and notes, MIT for the scripts (`LICENSE.md`).

## What the study found

1. **Jyotiṣa: an argued sphere** (report §1). Read: Āryabhaṭīya Gola 6–7 with Bhāskara I; Sūryasiddhānta 12;
   Pañcasiddhāntikā 13; Brāhmasphuṭasiddhānta 11 and 21 with Pṛthūdaka; Mahābhāskarīya 5.4 with Govindasvāmin and
   Parameśvara; Vaṭeśvara Gola 5; Mahāsiddhānta 16; Golādīpikā; Lalla's Śiṣyadhīvṛddhida 17 and 20; Bhāskara II's
   Golādhyāya with Vāsanā and Marīci. The anti-flat-earth polemic develops in sequence:
   - Varāhamihira and Brahmagupta argue only against rotation and the Jaina two suns.
   - Lalla (8th c.?) refutes a mirror-flat earth at length but leaves its holders anonymous.
   - Govindasvāmin and Pṛthūdaka (9th c.) set measured sizes and visible stars against the Purāṇic figures and a huge
     Meru.
   - Bhāskara II (12th c.) names the Purāṇa as the source of the flat earth, and Munīśvara (17th c.) quotes the
     Bhāgavata's own words.
   - Āryabhaṭa II instead maps the Purāṇic dvīpas onto the ball, and Parameśvara looks for a reconciliation.
2. **The Purāṇic *bhūgola* is the disc** (§2). Bhāgavata 5.16–25, copied by the Devībhāgavata; *bhūgola* as the label
   for dvīpa cosmography in the Nṛsiṃha and Nārada Purāṇas. The word is absent from Viṣṇu, Vāyu and Matsya in this
   corpus (not verified: the Bhāgavata may have taken a Jyotiṣa term for its own disc).
3. **The globe outside Jyotiṣa** (§3): Kumārila's relative up and down, ascribed to *purāṇa*; *bhūgolaka* as the
   largest earthy whole in Udayana, Śrīdhara and Gaṅgeśa; the *bhūgolanirṇaya* of Yogavāsiṣṭha Nirvāṇa 127, with
   Ānandabodhendra's list of seven views; Abhinavagupta's pole star; Kṣemarāja's ruling that Jyotiṣa holds for its own
   purpose but the Āgama is the real account.
4. **The Bhāgavata commentators on 5.16–22** (§4), from a new OCR of the 1965 Ahmedabad multi-commentary edition.
   Most read *bhūgola* as the 50-koṭi disc and just do the arithmetic. Three engage Jyotiṣa:
   - Vaṃśīdhara on 5.20.38: two earths, or yojanas of different sizes, citing Nīlakaṇṭha and a *Golādarśa*.
   - Jīva on 5.21.12, followed by Vaṃśīdhara: a parallax argument that makes Jyotiṣa's small solar circuit how the
     Purāṇa's distant sun looks from the ground.
   - Giridhara on 5.21.7: adopts the Jyotiṣa day-length method as not contrary to the Purāṇa.

   None of them adopts the spherical earth itself, except as Vaṃśīdhara's second, small earth.

## Files

| path | what it is |
|---|---|
| `results/bhugolaka/bhugolaka_shape_of_earth.md` | the report, with file and line references for every passage |
| `results/bhugolaka/bhugolaka.html` | the report as a page |
| `scripts/kwic.py` | regex KWIC over `1_sanskr/**/*.txt`; deduplicates near-identical contexts |
| `scripts/prox.py` | proximity search: hits for pattern A with pattern B within a set distance |
| `data/bhp5_16-20_commentaries_ks1965_vision_{deva,iast}.txt` | Google Vision OCR of the Bhāgavata Skandha 5 commentaries, PDF pp. 318–472, Devanāgarī and IAST, page-tagged `=== PDFPAGE n ===` (not in the public repository) |
| `data/bhp5_21-22_commentaries_ks1965_vision_{deva,iast}.txt` | the same for PDF pp. 473–514 (not in the public repository) |
| `data/kwic_bhp5_commentaries.txt` | KWIC over the 5.16–20 OCR, tagged by page and search term (*gola*, *vartula*, *kadamba*, *adhomukha* …) (not in the public repository) |
| `LICENSE.md`, `LICENSE-CC-BY-4.0.txt` | licence: CC BY 4.0 for the report and notes, MIT for the scripts |
| `data/kwic_nonjyot.txt` | *bhūgola(ka)* and its synonyms outside `8_jyot/` |
| `data/kwic_hyph.txt` | second pass for hyphenated forms (*bhū-gola*, *pṛthivī-golaka* …) |
| `data/kwic_yv.txt` | the Yogavāsiṣṭha passages and their parallels |
| `data/golakara.txt` | *golākāra / golākṛti* near earth words |
| `data/kadamba.txt` | *kadamba-puṣpa / kusuma* (the astronomers' image for the globe) |
| `data/flat.txt` | flat-shape terms (*chatrākāra*, *kūrmapṛṣṭha*, *ādarśa-tala*, *darpaṇodara*, *samatala*) near earth words |
| `data/jyot_vs.txt` | *jyotiḥśāstra / jyautiṣa / gaṇaka* near *bhūgola / bhūmaṇḍala / golākāra* |

The KWIC dumps are raw search output, kept for checking. Most hits in `flat.txt` and `kadamba.txt` are not about the
earth: levelling the ritual ground "like the inside of a mirror" (*bhūmiṃ samatalaṃ kṛtvā darpaṇodarasannibham*), the
*kadambagolakākāra* of Tantric visualisation, and the *kadambagolakanyāya* of how sound spreads.

## Method

- **Corpus search.** Regex over `1_sanskr/**/*.txt` for
  `(bhū|kṣiti|mahī|dharā|dharaṇī|pṛthvī|pṛthivī|bhūmi|ku)[-+ ]?gol…` (about 230 hits), then the proximity searches
  above. The searches were run on the Mac copy of `E-texts/1_sanskr` on 2026-10-31, and the report's line numbers are
  those of that copy.
- **Jyotiṣa texts.** Most of the Jyotiṣa editions in `1_sanskr/6_sastra/8_jyot/` were added on 2026-10-31 as
  uncorrected OCR. Quotations in the report are corrected by eye, and the report gives PDF pages for them.
- **Bhāgavata commentaries.** No commentary on Skandha 5 is in the corpus. The source is *Śrīmadbhāgavatam …
  anekavyākhyāsamalaṅkṛtam*, Skandha 5, ed. Kṛṣṇaśaṅkara Śāstrī (Ahmedabad 1965), archive.org
  `SrimadBhagavatamCanto05withMultipleSanskritCommentaries`. Archive.org's own OCR is unusable, so PDF pp. 318–514 were
  OCR'd with Google Vision and transliterated with `sanscript`. Printed page = PDF page − 2.

### Running the scripts

Run from the E-texts library root, since both scripts read `1_sanskr/` by relative path:

```sh
cd /mnt2/kengo/E-texts        # or the Mac copy
python3 ~/Documents/research/bhugolaka/scripts/kwic.py PATTERN [SKIP_PATH_REGEX] [WIDTH] > out.txt
python3 ~/Documents/research/bhugolaka/scripts/prox.py PATTERN_A PATTERN_B DISTANCE WIDTH [ROOT ...] > out.txt
```

`kwic.py` matches case-insensitively and gives `WIDTH` characters of context (default 160). `SKIP_PATH_REGEX` drops
files by path (e.g. `8_jyot` for the non-Jyotiṣa dump). `prox.py` keeps a hit for A only when B occurs within
`DISTANCE` characters; its roots default to `1_sanskr`.

## Open points

From the report's "Gaps" section:
- All the Jyotiṣa files are uncorrected OCR. The least certain reading is the Golādīpikā reconciliation (v. 33f.).
- The Śrīpati verse is quoted secondhand from Sharma's Vijñānabhāṣya; the Siddhāntaśekhara is not in the library.
- Unidentified: the cart-shaped / mirror-disc party in the Āryabhaṭīya commentary, and the *Golādarśa / Goladarpaṇa*
  Vaṃśīdhara cites.
- Whether the rotation passage in the Āryabhaṭīya commentary is Bhāskara I's or Someśvara's is not settled.
- Viśvanātha's promised *upapatti* for the 25-koṭi sun is not in 5.21–22; 5.23 and later are not checked.
- To check against the scan: the p. 485 passage, assigned to Giridhara from the nearest heading in the OCR.
- To check against the corpus: the Nīlakaṇṭha passage, against his Bhāratabhāvadīpa on the Bhīṣmaparvan.
