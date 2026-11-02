import os
from build_full_website import (
    get_global_head, get_global_nav, get_global_footer, get_cta_section,
    SVG_CHECK, SVG_PHONE, SVG_WHATSAPP, SVG_STAR, SVG_MAP_PIN, SVG_MAIL,
    SVG_SHIELD, SVG_SPINE, SVG_ACTIVITY, SVG_LASER, SVG_CROSSHAIR, SVG_HOME,
    SVG_HEART, SVG_CALENDAR, SVG_CHEVRON, SVG_ARROW_RIGHT, SVG_AWARD, SVG_CLOCK,
    SVG_WAVE, SVG_ZAP, SVG_NEEDLE, SVG_LAYERS
)

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Structured data for all 9 specialized services
SERVICES_DATA = [
    {
        "slug": "dorn-spinal-therapy",
        "title": "Dorn Method Spinal Alignment & Gentle Joint Therapy | Chromepet Chennai",
        "desc": "Non-invasive, gentle Dorn spinal alignment led by Dr. Prabhu Rajan, Vice Chairman of All India Dorn Therapy Association (AIDTA). Effective relief for slip disc, sciatica, scoliosis, and neck pain in Chromepet.",
        "kicker": "SPINAL CARE &bull; AIDTA VICE CHAIRMAN LED",
        "badge": "Vice Chairman, All India Dorn Therapy Association (AIDTA)",
        "icon": SVG_SPINE,
        "h1": "Gentle, non-manipulative spinal alignment for lasting pain relief.",
        "lead": "Unlike aggressive chiropractic cracking or temporary painkiller masking, the Dorn Method is an internationally respected, active-dynamic manual therapy that restores spinal vertebrae and joints to their natural anatomical alignment while the patient moves naturally.",
        "img": "clinic_consultation_area.jpg",
        "img_caption": "Dr. Prabhu Rajan's consultation room featuring Dorn spinal vertebrae & pelvic alignment charts.",
        "why_title": "Why the Dorn Method Excels over Conventional Manipulation",
        "why_text": "In conventional manipulation, the joint is thrust while the surrounding musculature is passive, triggering a reflexive defensive spasm. In the Dorn Method, Dr. Prabhu Rajan guides the patient into controlled rhythmic movements (such as swinging a leg or arm). This distracts the muscular neuromuscular guard, allowing the vertebrae to slip effortlessly back into place without trauma or ligament strain.",
        "steps": [
            ("Pelvic & Leg Length Assessment", "Checking for functional leg length discrepancy and iliosacral pelvic misalignment, which forms the true foundation of 85% of lumbar spinal distortions."),
            ("Dynamic Lumbar Realignment", "Correcting rotated or subluxated lumbar vertebrae during active swinging leg movements, opening compressed nerve roots safely."),
            ("Thoracic & Rib Alignment", "Realigning mid-back vertebrae and rib heads to relieve upper back tightness, scapular stabbing pain, and breathing discomfort."),
            ("Cervical Spine Balancing", "Gentle thumb pressure on cervical transverse processes during gentle head rotation to resolve neck pain, dizziness, and tension headaches.")
        ],
        "conditions": [
            ("Slip Disc & Lumbar Radiculopathy", "Decompresses pinched spinal nerve roots without surgical intervention, eliminating radiating numbness.", SVG_SPINE),
            ("Sciatica & Piriformis Syndrome", "Balances the sacrum and pelvis, releasing sciatic nerve impingement from the lumbar spine down to the foot.", SVG_CROSSHAIR),
            ("Cervical Spondylosis & Stiff Neck", "Restores normal cervical curvature and facet joint glide, relieving chronic stiffness and arm tingling.", SVG_ACTIVITY),
            ("Postural Scoliosis & Uneven Shoulders", "Gently guides asymmetrical spinal curves toward midline balance, improving functional posture.", SVG_SHIELD),
            ("Sacroiliac (SI) Joint Dysfunction", "Corrects pelvic rotation and joint shearing, relieving sharp stabbing pain when standing up or sitting down.", SVG_ZAP),
            ("Functional Leg Length Discrepancy", "Evens out hip height differences through simple, gentle hip and knee realignment maneuvers.", SVG_CHECK)
        ],
        "faqs": [
            ("Is Dorn spinal therapy painful or does it involve violent cracking?", "No. Dorn therapy involves zero sudden, high-velocity cracking or twisting. It is a gentle, bio-mechanical mobilization technique performed while you move your limb. Patients frequently report immediate sensation of lightness and relief."),
            ("How many Dorn sessions will I typically need?", "Most acute spinal and pelvic alignment issues experience significant improvement within 2 to 4 sessions. Chronic long-standing disc conditions may require 5 to 8 sessions combined with self-help home exercises."),
            ("Can older adults with osteoporosis receive Dorn therapy?", "Yes. Because there are no forceful thrusts, Dorn is one of the safest modalities for elderly patients, osteopenic individuals, and sensitive spines.")
        ]
    },
    {
        "slug": "laser-therapy",
        "title": "Advanced Scanning Laser Therapy (Class IV) | Chromepet Chennai | Rajan's Physio",
        "desc": "High-intensity scanning laser photobiomodulation at Rajan's Physiotherapy, Chromepet. Deep cellular healing for plantar fasciitis, tennis elbow, acute ligament tears, and nerve pain.",
        "kicker": "PHOTOBIOMODULATION &bull; CELLULAR REGENERATION",
        "badge": "LASERSTIM Scanning Console &bull; Deep Tissue Healing",
        "icon": SVG_LASER,
        "h1": "Deep photobiomodulation to accelerate tissue repair and kill pain.",
        "lead": "Our advanced scanning laser system delivers targeted coherent light energy deep into musculoskeletal tissues. It stimulates mitochondrial ATP production, quenches acute and chronic inflammation, and speeds cellular healing up to 40% faster than rest alone.",
        "img": "clinic_treatment_beds.jpg",
        "img_caption": "Scanning laser and electrotherapy suites at Rajan's Physiotherapy Centre, Chromepet.",
        "why_title": "The Biological Science of Scanning Laser Photobiomodulation",
        "why_text": "When monochromatic photons penetrate deep tissue layers, they are absorbed by Cytochrome C Oxidase in the cellular mitochondria. This triggers a surge in Adenosine Triphosphate (ATP) synthesis, releases nitric oxide to dilate local micro-capillaries, and suppresses pain-signaling bradykinin. The result is rapid cellular regeneration and immediate reduction in neurogenic pain.",
        "steps": [
            ("Anatomical Mapping", "Dr. Prabhu Rajan pinpoints the exact locus of ligament damage, tendon tear, or inflamed nerve root."),
            ("Targeted Photon Delivery", "The robotic scanning laser sweeps across the affected zone with controlled therapeutic joules/cm² of energy."),
            ("Cellular Biostimulation", "Photons activate mitochondrial metabolism, dramatically lowering local prostaglandins and swelling."),
            ("Rehabilitative Integration", "Coupled with gentle joint mobilization to lock in pain-free range of motion.")
        ],
        "conditions": [
            ("Plantar Fasciitis & Heel Spurs", "Accelerates micro-tear repair in the dense plantar fascia, eliminating sharp first-step morning heel pain.", SVG_LASER),
            ("Tennis Elbow & Golfer's Elbow", "Calms stubborn epicondylitis and stimulates collagen fiber alignment in forearm extensor tendons.", SVG_CROSSHAIR),
            ("Acute Ankle & Knee Sprains", "Rapidly reduces acute interstitial edema and swelling following sports injuries or missteps.", SVG_ACTIVITY),
            ("Carpal Tunnel Syndrome", "Reduces median nerve sheath inflammation at the wrist, resolving tingling, numbness, and grip weakness.", SVG_SHIELD),
            ("Achilles Tendinitis & Calf Strain", "Deep photon penetration stimulates stubborn, poorly vascularized tendon fibers toward rapid collagen synthesis.", SVG_ZAP),
            ("Post-Surgical Incision & Scar Recovery", "Softens dense surgical scar tissue, prevents keloids, and restores normal epidermal nerve sensation.", SVG_CHECK)
        ],
        "faqs": [
            ("Will I feel burning or electric shocks during scanning laser therapy?", "Not at all. The treatment is completely painless. You may feel a soothing, gentle biological warmth over the treated area as micro-circulation increases."),
            ("How long does each laser session take?", "A focused scanning laser session takes between 10 and 20 minutes depending on whether the condition is acute or chronic."),
            ("How soon will I notice relief?", "Many patients experience a noticeable decrease in pain and stiffness after the very first or second session, with cumulative regenerative benefits building over 4 to 6 sessions.")
        ]
    },
    {
        "slug": "shockwave-therapy",
        "title": "Radial Extracorporeal Shockwave Therapy (ESWT) | Chromepet Chennai",
        "desc": "Radial shockwave therapy in Chromepet, Chennai. Acoustic shockwaves break down calcific tendinitis, stubborn heel spurs, chronic Achilles tendinopathy, and deep myofascial adhesions.",
        "kicker": "ACOUSTIC PRESSURE WAVE &bull; 85%+ NON-SURGICAL SUCCESS",
        "badge": "Radial ESWT Technology &bull; Certified Orthopedic Protocols",
        "icon": SVG_WAVE,
        "h1": "Acoustic shockwaves to dissolve calcification and restart chronic healing.",
        "lead": "When chronic injuries have stalled in a sluggish, painful plateau for months or years, Radial Extracorporeal Shockwave Therapy (ESWT) delivers high-energy acoustic pulses that break down calcium deposits, stimulate angiogenesis (new blood vessels), and trigger a fresh biological healing cycle.",
        "img": "clinic_therapy_equipment.jpg",
        "img_caption": "Multi-modality shockwave and electrotherapy units at our Chromepet clinic.",
        "why_title": "How Shockwave Converts Chronic Degeneration into Active Healing",
        "why_text": "Chronic tendinopathies and heel spurs suffer from poor local vascularity and disorganized scar matrix. Radial shockwaves produce high mechanical tension and cavitation bubbles that physically break micro-calcifications and stimulate Substance P wash-out. This mobilizes mesenchymal stem cells and activates growth factors (VEGF, eNOS), restarting healthy tissue remodeling.",
        "steps": [
            ("Palpation & Acoustic Gel Application", "The exact epicenter of calcification or scar tissue is marked, and acoustic conductive gel is applied."),
            ("Radial Shockwave Pulses", "Controlled acoustic shock impulses (1.5 to 4.0 Bar pressure, 8-15 Hz) are directed into the stubborn tissue."),
            ("Cavitation & Micro-Vascularization", "Acoustic micro-trauma stimulates new capillary bud formation and disrupts pain transmitting C-nerve fibers."),
            ("Eccentric Loading & Functional Rehab", "Progressive tendon loading exercises ensure the new collagen matrix forms along lines of mechanical stress.")
        ],
        "conditions": [
            ("Calcific Tendinitis of the Shoulder", "Breaks down painful calcium deposits in the rotator cuff tendons without open or arthroscopic surgery.", SVG_WAVE),
            ("Stubborn Chronic Plantar Fasciitis", "Proven gold-standard intervention for heel pain that has failed rest, orthotics, and steroid injections.", SVG_CROSSHAIR),
            ("Chronic Achilles Tendinopathy", "Remodels thickened, degenerated Achilles tendon fibers, restoring pain-free running and stair climbing.", SVG_ACTIVITY),
            ("Patellar Tendinopathy (Jumper's Knee)", "Restores elasticity and high tensile strength to the patellar tendon in athletes and runners.", SVG_SHIELD),
            ("Greater Trochanteric Pain Syndrome", "Resolves chronic lateral hip bursitis and gluteal tendon tears that make sleeping on your side impossible.", SVG_ZAP),
            ("Deep Refractory Myofascial Trigger Points", "Deactivates dense, hyper-contracted muscular bands in the back and shoulder that resist manual massage.", SVG_CHECK)
        ],
        "faqs": [
            ("Is shockwave therapy painful?", "You will feel rhythmic thumping pulses over the tender point. Dr. Prabhu Rajan starts at a low intensity and adjusts the pressure precisely to your comfort threshold. Any mild discomfort subsides immediately once the pulse sequence ends."),
            ("How many sessions are typically required?", "Shockwave therapy is highly efficient: most patients require only 3 to 5 sessions, spaced 5 to 7 days apart."),
            ("Can I resume normal activities right after a shockwave session?", "Yes, you can walk and perform light daily tasks immediately. We simply advise avoiding intense plyometrics or heavy loading for 48 hours to allow the healing cascade to work.")
        ]
    },
    {
        "slug": "dry-needling",
        "title": "Certified Dry Needling Therapy (CDNT USA) | Chromepet Chennai | Dr. Prabhu Rajan",
        "desc": "Certified Dry Needling Therapist (CDNT USA) Dr. Prabhu Rajan in Chromepet. Precise myofascial trigger point deactivation for chronic muscle knots, tension headaches, and sciatica.",
        "kicker": "CDNT USA CERTIFIED &bull; INTRAMUSCULAR TRIGGER POINT RELEASE",
        "badge": "Certified Dry Needling Therapist (CDNT, USA)",
        "icon": SVG_NEEDLE,
        "h1": "Precision intramuscular trigger point release for deep muscle knots.",
        "lead": "Clinical Dry Needling uses ultra-fine, sterile filiform needles placed directly into hyper-irritable taut bands of muscle tissue (myofascial trigger points). This mechanical reset elicits a therapeutic 'local twitch response' that immediately halts chronic muscle spasm, restores blood flow, and eliminates referred pain.",
        "img": "clinic_treatment_room_1.jpg",
        "img_caption": "Clean, sanitized clinical examination and treatment room at Chromepet.",
        "why_title": "Dry Needling vs. Acupuncture: Understanding the Difference",
        "why_text": "While acupuncture is rooted in traditional Chinese meridian flow, Dry Needling is a strictly Western, evidence-based neuro-musculoskeletal medical intervention. Dr. Prabhu Rajan (certified CDNT USA) identifies contracted sarcomere knots through orthopedic palpation and targets the motor endplate directly, releasing trapped lactic acid and normalizing local biochemical pH.",
        "steps": [
            ("Trigger Point Identification", "Precise manual palpation to identify the exact taut band and reproduce the patient's referred pain pattern."),
            ("Sterile Insertion", "A single-use sterile micro-needle is gently guided through the skin into the hyperactive myofascial knot."),
            ("Local Twitch Response (LTR)", "The muscle briefly twitches and instantly releases, dropping electrical neuromuscular tension to zero."),
            ("Therapeutic Stretch & Hydration", "Passive elongation of the muscle fibers to restore full physiological length and mobility.")
        ],
        "conditions": [
            ("Upper Trapezius Knots & Tech Neck", "Releases rock-hard shoulder spasms caused by long desk hours and smartphone postural strain.", SVG_NEEDLE),
            ("Cervicogenic & Tension Headaches", "Deactivates suboccipital and sternocleidomastoid trigger points that refer pounding pain to the forehead.", SVG_CROSSHAIR),
            ("Piriformis Syndrome (Pseudo-Sciatica)", "Releases deep gluteal spasms that compress the sciatic nerve, eliminating buttock and thigh pain.", SVG_ACTIVITY),
            ("Chronic Low Back Muscle Guarding", "Resets tight quadratus lumborum and erector spinae muscles locked in chronic defensive guarding.", SVG_SHIELD),
            ("Tennis & Golfer's Forearm Tightness", "Deactivates extensor carpi radialis knots, restoring comfortable grip strength without elbow pain.", SVG_ZAP),
            ("Hamstring & Calf Cramping", "Eliminates chronic taut bands in runners and athletes prone to recurrent muscle tears and spasms.", SVG_CHECK)
        ],
        "faqs": [
            ("Does dry needling hurt?", "The needle is as thin as a human hair, so you barely feel the skin entry. When the needle reaches the trigger point, you will feel a brief dull ache or a split-second twitch, followed by an immediate sense of muscular release."),
            ("Are the needles reused?", "Never. We use 100% single-use, sterile, individually packaged surgical stainless-steel needles disposed of in medical sharps containers immediately after use."),
            ("Will I feel sore after the session?", "Some patients experience mild muscle soreness, similar to the feeling of a vigorous gym workout, for 12 to 24 hours. Applying heat and gentle stretching quickly resolves this.")
        ]
    },
    {
        "slug": "tecar-therapy",
        "title": "TECAR Therapy (Radiofrequency Diathermy) | Chromepet Chennai",
        "desc": "Deep capacitive and resistive radiofrequency diathermy (TECAR) in Chromepet. Accelerates cellular metabolism, relieves knee osteoarthritis, resolves acute hematomas and tendon injuries.",
        "kicker": "RADIOFREQUENCY DIATHERMY &bull; DEEP TISSUE HEALING",
        "badge": "Capacitive-Resistive Energy Transfer &bull; 448 kHz",
        "icon": SVG_ZAP,
        "h1": "Deep endogenous thermal energy for knee arthritis and athletic trauma.",
        "lead": "TECAR (Capacitive and Resistive Energy Transfer) utilizes high-frequency electromagnetic waves to activate natural cellular regeneration from within deep tissues. Unlike hot packs that only warm the skin surface, TECAR generates internal therapeutic heat inside dense ligaments, joint capsules, and deep muscle bellies.",
        "img": "clinic_treatment_beds.jpg",
        "img_caption": "Advanced diathermy and laser rehabilitation consoles at Rajan's Physiotherapy.",
        "why_title": "Capacitive vs. Resistive: Two Frequencies for Full-Depth Healing",
        "why_text": "TECAR utilizes two specialized handpieces: the Capacitive electrode concentrates energy in superficial, fluid-rich tissues (muscles, lymphatic vessels) to rapidly flush hematomas and edema; while the Resistive electrode concentrates energy into high-resistance fibrous tissues (tendons, ligaments, joint capsules, and periosteum) to stimulate collagen remodeling and deep joint mobility.",
        "steps": [
            ("Conductive Emulsion Application", "Medical-grade conductive cream is smoothed over the joint or muscle group to ensure optimal impedance match."),
            ("Capacitive Soft Tissue Phase", "Gentle circular movements stimulate lymphatic drainage and relieve surrounding muscle spasm."),
            ("Resistive Deep Joint Phase", "Deep targeted electromagnetic transfer into the joint capsule, tendon insertions, or arthritic cartilage."),
            ("Active Functional Mobilization", "Performing range-of-motion exercises while the tissue is warm, pliable, and fully oxygenated.")
        ],
        "conditions": [
            ("Knee Osteoarthritis & Cartilage Wear", "Stimulates synovial fluid secretion, reduces morning joint stiffness, and eases walking pain.", SVG_ZAP),
            ("Acute Sports Muscle Tears & Hematomas", "Increases local lymphatic flow by up to 300%, draining severe bruises and hematomas in days.", SVG_CROSSHAIR),
            ("Frozen Shoulder (Adhesive Capsulitis)", "Softens the fibrotic, contracted shoulder capsule, restoring overhead arm reach and sleep comfort.", SVG_ACTIVITY),
            ("Post-Fracture Joint Stiffness", "Mobilizes tight contractures around healed bone fractures, speeding return to normal limb function.", SVG_SHIELD),
            ("Rotator Cuff & Supraspinatus Tendinitis", "Deep resistive energy accelerates vascular repair in the notoriously blood-poor rotator cuff zone.", SVG_WAVE),
            ("Post-Operative Swelling & Edema", "Rapidly reduces severe post-surgical fluid accumulation without uncomfortable pressure.", SVG_CHECK)
        ],
        "faqs": [
            ("What does a TECAR therapy session feel like?", "It feels like a warm, deeply relaxing internal massage. Patients often find it exceptionally pleasant and experience an immediate decrease in joint stiffness."),
            ("How many sessions are recommended for knee osteoarthritis?", "A course of 6 to 10 sessions typically yields profound pain reduction, improved walking tolerance, and significant delay or prevention of joint replacement surgery."),
            ("Is TECAR safe for patients with metal implants or pacemakers?", "TECAR is safe around titanium orthopedic plates and screws under resistive mode. However, like all electromagnetic therapies, it is contraindicated for patients with cardiac pacemakers or during pregnancy.")
        ]
    },
    {
        "slug": "cupping-iastm",
        "title": "Kinesio Cupping & IASTM Soft Tissue Mobilization | Chromepet Chennai",
        "desc": "Negative pressure myofascial cupping and precision stainless-steel IASTM blade therapy in Chromepet. Releases fascial adhesions, promotes lymphatic drainage, and speeds athletic recovery.",
        "kicker": "FASCIAL DECOMPRESSION &bull; INSTRUMENT-ASSISTED MOBILIZATION",
        "badge": "Myofascial Decompression &bull; Medical Stainless Steel",
        "icon": SVG_LAYERS,
        "h1": "Decompress tight fascia and dissolve stubborn scar tissue.",
        "lead": "While most therapies compress tissues inward, Kinesio Cupping uses therapeutic negative suction pressure to lift skin and superficial fascia away from the muscle, creating room for micro-circulation and lymphatic drainage. Combined with IASTM (Instrument-Assisted Soft Tissue Mobilization) stainless steel contour blades, it breaks down restrictive adhesions.",
        "img": "clinic_consultation_area.jpg",
        "img_caption": "Manual therapy and postural correction station at our Chromepet practice.",
        "why_title": "Why Fascial Restriction Causes Persistent, Mysterious Aches",
        "why_text": "Fascia is an interconnected 3D spiderweb of connective tissue enveloping every muscle, nerve, and bone. After an injury or years of poor posture, fascia dehydrates and forms microscopic cross-links and adhesions that restrict joint glide and squeeze pain receptors. By combining negative suction cupping with bevel-edged IASTM instruments, Dr. Prabhu Rajan rehydrates the fascial plane and restores effortless movement.",
        "steps": [
            ("Fascial Restriction Scanning", "Using ergonomic stainless steel instruments to detect gravelly tissue textures and fascial densification."),
            ("IASTM Cross-Fiber Friction", "Controlled, gentle micro-strokes stimulate fibroblast proliferation and realign disorganized collagen."),
            ("Dynamic Kinesio Cupping", "Placing suction cups over restricted meridian lines and guiding active joint movements to decompress the layers."),
            ("Myofascial Flush & Mobility", "Flushing out liberated metabolic waste and integrating full functional range of motion.")
        ],
        "conditions": [
            ("Ilio-Tibial (IT) Band Friction Syndrome", "Decompresses the dense lateral fascia of the thigh, eliminating sharp stabbing knee pain in runners.", SVG_LAYERS),
            ("Post-Surgical Scar Tissue Mobilization", "Softens and loosens thick, puckered scars after abdominal, orthopedic, or spine surgeries.", SVG_CROSSHAIR),
            ("Chronic Mid-Back & Scapular Tightness", "Releases deep fascial tension between the shoulder blades caused by computer hunching.", SVG_ACTIVITY),
            ("Plantar Fascial Densification", "IASTM contour blades break down rigid adhesions along the arch of the foot, restoring flexibility.", SVG_SHIELD),
            ("Thoracic Spine & Rib Stiffness", "Dynamic cupping expands ribcage excursion, improving deep breathing and spinal rotation.", SVG_ZAP),
            ("Post-Workout Athletic Fatigue", "Accelerates removal of lactic acid and metabolic byproducts, cutting athletic recovery times in half.", SVG_CHECK)
        ],
        "faqs": [
            ("Will cupping leave marks on my skin?", "Cupping frequently produces circular reddish or purplish discoloration. These are NOT bruises (which indicate broken capillaries from trauma); rather, they are cellular debris and stagnant blood drawn to the surface for lymphatic removal. They fade completely within 3 to 7 days."),
            ("Does IASTM blade scraping damage healthy tissue?", "Not at all. The instruments have rounded, medical-grade beveled edges designed strictly to resonate against abnormal fibrotic tissue without cutting or damaging healthy skin."),
            ("Can cupping be combined with other treatments?", "Yes! At Rajan's Physio, we frequently combine dynamic cupping with Dorn spinal alignment and laser therapy for a complete, synergistic recovery.")
        ]
    },
    {
        "slug": "electrotherapy",
        "title": "Advanced Electrotherapy, IFT & Ultrasound Therapy | Chromepet Chennai",
        "desc": "Multi-channel Interferential Therapy (IFT), TENS, therapeutic ultrasound (Electroson 608), and spinal traction at Rajan's Physiotherapy Chromepet. Fast relief for nerve and joint pain.",
        "kicker": "CLINICAL MODALITIES &bull; PROVEN SYMPTOM RESOLUTION",
        "badge": "Electroson 608 Ultrasound &bull; 4-Pole Interferential IFT",
        "icon": SVG_ACTIVITY,
        "h1": "Targeted electrotherapy and ultrasound to soothe acute nerve and joint pain.",
        "lead": "Equipped with state-of-the-art multi-channel clinical consoles (including our Electroson 608 unit), our electrotherapy suite delivers precision electrical and acoustic waves that block pain signals at the spinal gate, promote ultrasonic acoustic micromassage, and re-educate weakened muscles.",
        "img": "clinic_therapy_equipment.jpg",
        "img_caption": "Authentic clinical photograph of the Electroson 608 ultrasound and electrotherapy suite at Chromepet.",
        "why_title": "The Dual Action of IFT and Therapeutic Ultrasound",
        "why_text": "Interferential Therapy (IFT) crosses two medium-frequency electrical currents inside deep tissues to produce a low-frequency therapeutic beat. This activates the spinal Gate Control mechanism, flooding the nervous system with endorphins and reducing deep muscular spasms without painful skin irritation. Therapeutic ultrasound (1 MHz & 3 MHz) simultaneously vibrates cellular membranes at 1 million cycles per second, increasing cell permeability and accelerating healing.",
        "steps": [
            ("Neuromuscular Evaluation", "Dr. Prabhu Rajan assesses whether your pain originates from sensory nerve irritation, motor deficit, or acute bursitis."),
            ("Frequency & Intensity Calibration", "Setting exact waveform parameters (vector sweep, burst mode, or continuous ultrasound beam)."),
            ("Therapeutic Application", "Relaxing on our cushioned therapy couches while electrical currents modulate nerve transmission."),
            ("Functional Muscle Activation", "Combining neuromuscular electrical stimulation with voluntary contractions to reverse disuse atrophy.")
        ],
        "conditions": [
            ("Cervical & Lumbar Spondylosis", "Deep penetrating IFT currents soothe irritated nerve roots and relieve chronic spine aches.", SVG_ACTIVITY),
            ("Bell's Palsy & Facial Nerve Rehabilitation", "Specialized galvanic and faradic stimulation to retrain paralyzed facial muscles to blink, smile, and speak.", SVG_CROSSHAIR),
            ("Acute Bursitis & Synovitis", "Therapeutic ultrasound rapidly disperses inflammatory fluid pockets around shoulders and hips.", SVG_SHIELD),
            ("Post-Fracture Muscle Atrophy", "Neuromuscular Electrical Stimulation (NMES) rebuilds quadriceps or calf bulk after cast removal.", SVG_ZAP),
            ("Acute Muscle Spasms & Wry Neck (Torticollis)", "IFT breaks the painful spasm-pain-spasm cycle, allowing gentle range of motion to return.", SVG_SPINE),
            ("Sciatica & Nerve Root Entrapment", "Modulates pain signals traveling down the leg while reducing local perineural swelling.", SVG_CHECK)
        ],
        "faqs": [
            ("What does IFT feel like?", "IFT produces a pleasant, rhythmic tingling sensation. It should never feel sharp or painful. Our therapists calibrate the current precisely to your comfort level."),
            ("How does ultrasound therapy differ from diagnostic ultrasound scans?", "Diagnostic ultrasound takes pictures of internal organs using sound reflections. Therapeutic ultrasound uses a higher-energy sound beam to produce gentle biological warmth and microscopic cell massage that accelerates tissue healing."),
            ("Can pregnant women receive electrotherapy?", "Electrotherapy is generally avoided over the abdomen and lower back during pregnancy. However, our therapists offer safe manual therapy and Dorn method pelvic balancing as alternatives.")
        ]
    },
    {
        "slug": "sports-rehabilitation",
        "title": "Sports Injury & Orthopedic Rehabilitation | Chromepet Chennai | Dr. Prabhu Rajan MPT",
        "desc": "Specialized sports physiotherapy by Dr. Prabhu Rajan, Master of Physiotherapy in Sports (MPT Sports 2013). ACL rehab, rotator cuff tears, sprains, and return-to-sport training in Chromepet.",
        "kicker": "MPT SPORTS (2013) &bull; RETURN-TO-PLAY ATHLETIC REHAB",
        "badge": "Master of Physiotherapy in Sports &bull; MIAP L-27944",
        "icon": SVG_AWARD,
        "h1": "Elite sports injury rehabilitation and return-to-play conditioning.",
        "lead": "Led by Dr. Prabhu Rajan, PT—holding a Master of Physiotherapy in Sports (MPT Sports 2013) with 17 years of experience treating athletes, cricket players, badminton enthusiasts, and fitness pros—we offer structured, phase-based rehabilitation that restores explosive power, joint stability, and prevents re-injury.",
        "img": "dr_prabhu_rajan_profile.jpg",
        "img_caption": "Dr. Prabhu Rajan, PT (MPT Sports, Dr.Acu, CDNT USA, Vice Chairman AIDTA).",
        "why_title": "The 4-Phase Sports Rehabilitation Framework",
        "why_text": "Athletes cannot afford partial recoveries. A prematurely rehabilitated ligament is twice as likely to re-tear. Our sports medicine protocol takes you through four distinct phases: Acute Protection & Inflammation Control, Restoring Full Biomechanical Range, Progressive Eccentric Strength & Proprioception, and Sport-Specific Plyometric Conditioning before issuing a formal Return-to-Play clearance.",
        "steps": [
            ("Phase 1: Protection & Swelling Control", "Using Class IV laser, gentle lymphatic drainage, and cryotherapy to arrest acute joint effusion."),
            ("Phase 2: Mobility & Joint Mechanics", "Restoring full passive and active range of motion without compensating at neighboring joints."),
            ("Phase 3: Proprioception & Kinetic Chain Loading", "Wobble board drills, single-leg balance, and eccentric loading to rebuild joint stability and neuromuscular speed."),
            ("Phase 4: Sport-Specific Conditioning", "Agility ladders, cutting drills, acceleration-deceleration testing, and psychological confidence building.")
        ],
        "conditions": [
            ("ACL & Meniscus Post-Surgical Rehab", "Structured 6-to-9 month protocol to restore full knee flexion, quadriceps girth, and pivot-shift stability.", SVG_AWARD),
            ("Rotator Cuff Tears & Shoulder Impingement", "Rebalances the scapulothoracic rhythm in badminton, cricket fast bowlers, and tennis players.", SVG_CROSSHAIR),
            ("Inversion Ankle Sprains & Ligament Laxity", "Rebuilds peroneal muscle reactivity and lateral ligament integrity to eliminate recurrent rolling.", SVG_ACTIVITY),
            ("Hamstring & Groin Muscle Strains", "High-speed eccentric hamstring loading protocols to prevent nagging recurrence during sprinting.", SVG_SHIELD),
            ("Patellofemoral Pain Syndrome (Runner's Knee)", "Corrects hip abductor weakness, vastus medialis delay, and foot overpronation.", SVG_ZAP),
            ("Cricket Fast Bowling Lumbar Stress Rehab", "Core stability, pelvic control, and bowling action kinetic analysis to offload lumbar pars interarticularis.", SVG_CHECK)
        ],
        "faqs": [
            ("I had ACL reconstruction surgery. When should I begin physiotherapy?", "Rehabilitation should begin within the first 48 to 72 hours post-surgery for gentle ankle pumps, quadriceps activation, and swelling control. The first 6 weeks are critical for regaining full knee extension."),
            ("Do you treat recreational weekend athletes or only professionals?", "We treat athletes of all levels! Whether you play competitive cricket, run marathons, play weekend badminton, or work out at the gym, our sports rehabilitation protocols are tailored to your specific athletic goals."),
            ("How do you determine when it is safe to return to competitive sports?", "We do not guess. We conduct objective functional testing, including limb symmetry index (LSI), single-leg hop tests, Y-balance tests, and sport-specific agility drills before granting full clearance.")
        ]
    },
    {
        "slug": "home-physiotherapy",
        "title": "Dedicated In-Home Physiotherapy Program | Chromepet, Pallavaram, Tambaram",
        "desc": "Expert in-home physiotherapy visits across Chromepet, Pallavaram, and Tambaram by Rajan's Physiotherapy Centre. Post-surgery, stroke recovery, and geriatric care directly at your bedside.",
        "kicker": "DOORSTEP HEALTHCARE &bull; CHROMPEPET, PALLAVARAM & TAMBARAM",
        "badge": "Doctor-Supervised In-Home Visits &bull; Portable Equipment",
        "icon": SVG_HOME,
        "h1": "Doctor-led physiotherapy delivered directly to your home bedside.",
        "lead": "When severe pain, post-surgical weakness, stroke hemiplegia, or elderly frailty makes traveling to a clinic painful or unsafe, Rajan's Physiotherapy brings hospital-grade clinical rehabilitation directly to your residence with our dedicated in-home care team.",
        "img": "clinic_entrance.jpg",
        "img_caption": "Rajan's Physiotherapy Centre headquarters in Chromepet, coordinating home care visits daily.",
        "why_title": "Why In-Home Physiotherapy is Essential for Certain Conditions",
        "why_text": "Navigating stairs, getting into cars, and sitting in traffic immediately following major joint replacements or spinal surgeries can aggravate swelling and risk joint dislocation. Our therapists arrive with portable ultrasound, TENS/IFT, needling, and exercise bands, allowing patients to recover in the comfort, hygiene, and dignity of their own home under direct family supervision.",
        "steps": [
            ("Home Visit Booking & Pre-Assessment", "Contact our Chromepet clinic via phone or WhatsApp. We review your discharge summary, MRI, or doctor's prescription."),
            ("Initial Bedside Examination", "Our experienced physiotherapist conducts a thorough in-home evaluation of joint mobility, pain levels, and home safety."),
            ("Hands-On Bedside Therapy", "Administering modalities, passive range-of-motion, gait retraining, and transfer training right in your bedroom or living room."),
            ("Family & Caregiver Education", "Teaching family members safe lifting techniques, bed positioning to prevent bedsores, and home exercise assistance.")
        ],
        "conditions": [
            ("Post-Total Knee & Hip Replacement (TKR/THR)", "Immediate post-operative mobilization, walking aid weaning, and continuous passive motion in your bedroom.", SVG_HOME),
            ("Stroke, Paralysis & Hemiplegia Recovery", "Neuro-developmental therapy (NDT) to retrain arm and leg motor control, balance, and independent standing.", SVG_CROSSHAIR),
            ("Geriatric Mobility & Fall Prevention", "Gently rebuilds muscle strength and balance confidence for elderly parents who have become bed-bound or fearful of falling.", SVG_ACTIVITY),
            ("Severe Acute Slip Disc & Sciatica", "When acute back spasms make walking or sitting in a car impossible, we deliver pain-relieving therapy to your bed.", SVG_SHIELD),
            ("Parkinson's Disease Mobility Training", "Rhythmic auditory cueing, trunk rotation, and gait-lengthening drills to overcome freezing of gait.", SVG_ZAP),
            ("Post-Fracture Bedside Rehabilitation", "Safe, doctor-guided weight-bearing progression and range-of-motion restoration following plaster removal or surgical plating.", SVG_CHECK)
        ],
        "faqs": [
            ("Which Chennai localities do your home visit teams cover?", "We cover Chromepet, Pallavaram, Tambaram (East & West), Chitlapakkam, Hasthinapuram, Radha Nagar, Nemilichery, and adjoining South Chennai neighborhoods."),
            ("What equipment does the visiting physiotherapist bring?", "Our therapists bring portable therapeutic ultrasound, digital TENS/IFT units, resistance bands, dry needling supplies, and pulse oximeters directly to your home."),
            ("What is the cost of an in-home physiotherapy session?", "Home visit sessions range between ₹800 and ₹1,200 per visit depending on distance from our Chromepet clinic and complexity of care. Discounted weekly and monthly packages are available.")
        ]
    }
]

print(f"Loaded {len(SERVICES_DATA)} specialized clinical services.")

def render_service_page(service, depth_prefix):
    asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"
    home_link = depth_prefix if depth_prefix else "./"
    if not home_link.endswith(('/', 'index.html')):
        home_link = home_link + "index.html" if home_link else "./index.html"
    
    # Generate conditions grid
    conditions_html = ""
    for idx, (name, desc, icon) in enumerate(service["conditions"], start=1):
        stagger_class = f"stagger-{(idx % 6) or 6}"
        conditions_html += f"""          <div class="service-card reveal-blur {stagger_class}" style="padding:26px;">
            <div>
              <div style="width:48px; height:48px; border-radius:12px; background:#EEF3FA; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
                {icon}
              </div>
              <h3 style="font-family:'Recoleta',Georgia,serif; font-size:20px; line-height:1.26 !important; color:#233E85 !important; margin-bottom:10px;">
                {name}
              </h3>
              <p style="font-size:14px; line-height:1.6 !important; color:#4A5568 !important; margin:0;">
                {desc}
              </p>
            </div>
            <div style="margin-top:20px; padding-top:14px; border-top:1px solid #EEF2F4; display:flex; align-items:center; gap:6px; font-size:12.5px; font-weight:600; color:#233E85;">
              {SVG_CHECK} Clinically Resolved
            </div>
          </div>\n"""

    # Generate steps HTML
    steps_html = ""
    for idx, (step_title, step_desc) in enumerate(service["steps"], start=1):
        stagger_class = f"stagger-{idx}"
        steps_html += f"""          <div class="bento-card reveal-blur {stagger_class}" style="padding:26px;">
            <div style="display:flex; align-items:center; gap:14px; margin-bottom:14px;">
              <div style="width:38px; height:38px; border-radius:50%; background:#233E85; color:#FBF5E9; display:flex; align-items:center; justify-content:center; font-family:'Recoleta',Georgia,serif; font-size:18px; font-weight:700; flex-shrink:0;">
                {idx}
              </div>
              <h4 style="font-family:'Recoleta',Georgia,serif; font-size:18px; line-height:1.28 !important; color:#233E85 !important; margin:0;">
                {step_title}
              </h4>
            </div>
            <p style="font-size:14px; line-height:1.6 !important; color:#4A5568 !important; margin:0;">
              {step_desc}
            </p>
          </div>\n"""

    # Generate FAQs HTML
    faqs_html = ""
    for idx, (q, a) in enumerate(service["faqs"], start=1):
        faqs_html += f"""          <div class="faq-item reveal-blur stagger-{idx}">
            <div class="faq-q">
              <span>{q}</span>
              <span class="faq-icon">+</span>
            </div>
            <div class="faq-a">
              {a}
            </div>
          </div>\n"""

    html = f"""{get_global_head(service["title"], service["desc"], asset_prefix)}
{get_global_nav(depth_prefix, "services")}

  <main>
    <!-- HERO SECTION -->
    <section class="section section--hero" style="background:#FAF6EE; padding:60px 0 72px 0;">
      <div class="container w-container">
        <!-- BREADCRUMB -->
        <div style="font-size:12px; font-weight:600; letter-spacing:0.8px; text-transform:uppercase; margin-bottom:18px; color:#536B88; display:flex; align-items:center; gap:8px;">
          <a href="{home_link}" style="color:#536B88; text-decoration:none;">Home</a>
          <span>/</span>
          <span style="color:#233E85;">Services</span>
          <span>/</span>
          <span style="color:#233E85; font-weight:700;">{service["slug"].replace('-', ' ').title()}</span>
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:48px; align-items:center;">
          <div>
            <div class="clinic-badge">
              {service["icon"]} {service["badge"]}
            </div>
            <h1 style="font-family:'Recoleta',Georgia,serif; font-size:clamp(30px, 3.8vw, 44px); line-height:1.18 !important; color:#233E85 !important; margin-bottom:16px;">
              {service["h1"]}
            </h1>
            <p style="font-size:16px; line-height:1.65 !important; color:#4A5568 !important; margin-bottom:24px;">
              {service["lead"]}
            </p>
            
            <div style="display:flex; flex-wrap:wrap; gap:16px; margin-bottom:28px;">
              <div style="display:flex; align-items:center; gap:8px; font-size:14px; font-weight:600; color:#233E85;">
                {SVG_CHECK} 100% Non-Surgical
              </div>
              <div style="display:flex; align-items:center; gap:8px; font-size:14px; font-weight:600; color:#233E85;">
                {SVG_CHECK} Led by Dr. Prabhu Rajan, PT
              </div>
              <div style="display:flex; align-items:center; gap:8px; font-size:14px; font-weight:600; color:#233E85;">
                {SVG_CHECK} Rapid Lasting Relief
              </div>
            </div>

            <div style="display:flex; flex-wrap:wrap; gap:14px;">
              <a href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20consult%20regarding%20{service['slug']}" target="_blank" class="btn-whatsapp">
                {SVG_WHATSAPP} Book WhatsApp Consultation
              </a>
              <a href="tel:9042612895" class="btn-secondary">
                {SVG_PHONE} Call +91 90426 12895
              </a>
            </div>
          </div>

          <div>
            <div class="photo-card" style="">
              <img src="{asset_prefix}images/{service['img']}" alt="{service['title']}" style="width:100%; height:340px; object-fit:cover; display:block;" loading="eager"/>
              <div style="padding:18px 22px; background:#FFFFFF; border-top:1px solid #EEF2F4;">
                <p style="font-size:13px; line-height:1.55; color:#536B88; margin:0;">
                  <strong>Chromepet Practice:</strong> {service['img_caption']}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- WHY THIS THERAPY SECTION -->
    <section class="section" style="background:#FFFFFF; padding:72px 0;">
      <div class="container w-container">
        <div style="max-width:760px; margin:0 auto 48px auto; text-align:center;">
          <div class="section-kicker">{service["kicker"]}</div>
          <h2 style="font-family:'Recoleta',Georgia,serif; font-size:clamp(26px, 3.2vw, 36px); line-height:1.22 !important; color:#233E85 !important; margin-bottom:14px;">
            {service["why_title"]}
          </h2>
          <p style="font-size:15.5px; line-height:1.65 !important; color:#4A5568 !important; margin:0;">
            {service["why_text"]}
          </p>
        </div>

        <!-- 4-STEP PROTOCOL -->
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap:24px;">
{steps_html}        </div>
      </div>
    </section>

    <!-- CONDITIONS TREATED BENTO GRID -->
    <section class="section" style="background:#FAF6EE; padding:72px 0;">
      <div class="container w-container">
        <div style="text-align:center; max-width:720px; margin:0 auto 48px auto;">
          <div class="section-kicker">TARGETED CLINICAL RELIEF</div>
          <h2 style="font-family:'Recoleta',Georgia,serif; font-size:clamp(26px, 3.2vw, 36px); line-height:1.22 !important; color:#233E85 !important; margin-bottom:14px;">
            Conditions effectively resolved at our clinic.
          </h2>
          <p style="font-size:15.5px; line-height:1.6 !important; color:#4A5568 !important; margin:0;">
            Every patient receives an individual biomechanical evaluation. We treat the foundational cause of your impairment rather than merely silencing symptoms.
          </p>
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:24px;">
{conditions_html}        </div>
      </div>
    </section>

    <!-- DOCTOR & CLINIC CREDENTIALS CALLOUT -->
    <section class="section" style="background:#FFFFFF; padding:64px 0;">
      <div class="container w-container">
        <div style="background:#EEF3FA; border-radius:22px; padding:38px 44px; display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:32px; align-items:center;">
          <div>
            <span style="font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:#233E85;">DOCTOR SUPERVISION</span>
            <h3 style="font-family:'Recoleta',Georgia,serif; font-size:26px; line-height:1.24 !important; color:#233E85 !important; margin:10px 0 14px 0;">
              Supervised directly by Dr. Prabhu Rajan, PT
            </h3>
            <p style="font-size:14.5px; line-height:1.6 !important; color:#334E54 !important; margin-bottom:18px;">
              With 17 years of specialized practice, Dr. Prabhu Rajan personally conducts every initial biomechanical evaluation, formulates your therapy plan, and monitors your progress every session.
            </p>
            <div style="display:flex; flex-wrap:wrap; gap:16px; font-size:13.5px; font-weight:600; color:#233E85;">
              <span>&bull; MIAP L-27944</span>
              <span>&bull; MPT Sports (2013)</span>
              <span>&bull; CDNT (USA)</span>
              <span>&bull; Vice Chairman AIDTA</span>
            </div>
          </div>
          <div style="text-align:right;">
            <div style="display:inline-block; background:#FFFFFF; border-radius:18px; padding:24px 28px; text-align:left; ">
              <div style="display:flex; align-items:center; gap:6px; margin-bottom:8px;">
                {SVG_STAR}{SVG_STAR}{SVG_STAR}{SVG_STAR}{SVG_STAR}
                <span style="font-weight:700; font-size:14px; color:#233E85; margin-left:4px;">5.0 / 5.0</span>
              </div>
              <p style="font-size:13.5px; line-height:1.55; color:#4A5568; margin-bottom:12px; font-style:italic;">
                "Dr. Prabhu's treatment for my back and spine gave me life-changing relief after months of suffering. Very gentle and thorough."
              </p>
              <p style="font-size:12.5px; font-weight:700; color:#233E85; margin:0;">
                &mdash; Verified Patient Review (Practo &bull; 99% Recommended)
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ SECTION -->
    <section class="section" style="background:#FAF6EE; padding:64px 0;">
      <div class="container w-container" style="max-width:820px;">
        <div style="text-align:center; margin-bottom:36px;">
          <div class="section-kicker">COMMON QUESTIONS</div>
          <h2 style="font-family:'Recoleta',Georgia,serif; font-size:clamp(24px, 3vw, 34px); line-height:1.22 !important; color:#233E85 !important; margin:0;">
            Frequently Asked Questions
          </h2>
        </div>

        <div>
{faqs_html}        </div>
      </div>
    </section>

{get_cta_section(depth_prefix)}
  </main>

{get_global_footer(depth_prefix)}"""
    return html


# Contact Page Generator
def render_contact_page(depth_prefix):
    asset_prefix = f"{depth_prefix}assets/" if depth_prefix else "assets/"
    home_link = depth_prefix if depth_prefix else "./"
    if not home_link.endswith(('/', 'index.html')):
        home_link = home_link + "index.html" if home_link else "./index.html"

    title = "Contact & Clinic Location | Rajan's Physiotherapy Chromepet Chennai"
    desc = "Visit Rajan's Physiotherapy & Pain Relief Centre in Chromepet, Chennai. Behind Chromepet Police Station. Call +91 90426 12895 or book via WhatsApp."

    return f"""{get_global_head(title, desc, asset_prefix)}
{get_global_nav(depth_prefix, "contact")}

  <main>
    <!-- HERO SECTION -->
    <section class="section section--hero" style="background:#FAF6EE; padding:60px 0 64px 0;">
      <div class="container w-container">
        <!-- BREADCRUMB -->
        <div style="font-size:12px; font-weight:600; letter-spacing:0.8px; text-transform:uppercase; margin-bottom:18px; color:#536B88; display:flex; align-items:center; gap:8px;">
          <a href="{home_link}" style="color:#536B88; text-decoration:none;">Home</a>
          <span>/</span>
          <span style="color:#233E85; font-weight:700;">Contact &amp; Clinic Location</span>
        </div>

        <div style="max-width:760px; margin-bottom:36px;">
          <div class="clinic-badge">
            {SVG_MAP_PIN} Chromepet, Chennai &bull; Est. 2009
          </div>
          <h1 style="font-family:'Recoleta',Georgia,serif; font-size:clamp(32px, 4vw, 44px); line-height:1.18 !important; color:#233E85 !important; margin-bottom:16px;">
            Visit our clinic or speak directly with our team.
          </h1>
          <p style="font-size:16px; line-height:1.65 !important; color:#4A5568 !important; margin:0;">
            Conveniently situated in Chromepet, Chennai (behind Chromepet Police Station), Rajan's Physiotherapy &amp; Pain Relief Centre provides clinical excellence and a welcoming, supportive healing environment.
          </p>
        </div>

        <!-- 3-COL CONTACT DETAILS -->
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:24px; margin-bottom:48px;">
          <!-- CARD 1: LOCATION -->
          <div class="bento-card reveal-blur stagger-1" style="padding:28px;">
            <div style="width:44px; height:44px; border-radius:12px; background:#EEF3FA; display:flex; align-items:center; justify-content:center; margin-bottom:16px;">
              {SVG_MAP_PIN}
            </div>
            <h3 style="font-family:'Recoleta',Georgia,serif; font-size:20px; line-height:1.26 !important; color:#233E85 !important; margin-bottom:10px;">
              Clinic Address
            </h3>
            <p style="font-size:14.5px; line-height:1.6 !important; color:#4A5568 !important; margin-bottom:14px;">
              <strong>No. 9 / 29C, 1st Cross Street</strong>,<br>
              Nagappa Nagar / New Colony,<br>
              Chromepet, Chennai &ndash; 600044<br>
              <span style="font-size:13px; color:#718096;">(Landmark: Behind Chromepet Police Station / Shastri Colony)</span>
            </p>
            <a href="https://share.google/tpyR96H2jyHYaLHxz" target="_blank" class="btn-secondary" style="font-size:13px; padding:8px 18px;">
              Open in Google Maps &rarr;
            </a>
          </div>

          <!-- CARD 2: PHONE & WHATSAPP -->
          <div class="bento-card reveal-blur stagger-2" style="padding:28px;">
            <div style="width:44px; height:44px; border-radius:12px; background:#EEF3FA; display:flex; align-items:center; justify-content:center; margin-bottom:16px;">
              {SVG_PHONE}
            </div>
            <h3 style="font-family:'Recoleta',Georgia,serif; font-size:20px; line-height:1.26 !important; color:#233E85 !important; margin-bottom:10px;">
              Phone &amp; WhatsApp
            </h3>
            <p style="font-size:14.5px; line-height:1.6 !important; color:#4A5568 !important; margin-bottom:14px;">
              <strong>Primary Phone:</strong> <a href="tel:9042612895" style="color:#233E85; font-weight:600; text-decoration:none;">+91 90426 12895</a><br>
              <strong>Alternate Phone:</strong> <a href="tel:9840512895" style="color:#233E85; text-decoration:none;">+91 98405 12895</a><br>
              <strong>WhatsApp:</strong> <a href="https://wa.me/919042612895" target="_blank" style="color:#25D366; font-weight:600; text-decoration:none;">+91 90426 12895</a>
            </p>
            <a href="https://wa.me/919042612895?text=Hello%20Dr.%20Prabhu%2C%20I%20would%20like%20to%20book%20an%20appointment" target="_blank" class="btn-whatsapp" style="font-size:13px; padding:8px 18px;">
              {SVG_WHATSAPP} Chat on WhatsApp
            </a>
          </div>

          <!-- CARD 3: HOURS -->
          <div class="bento-card reveal-blur stagger-3" style="padding:28px;">
            <div style="width:44px; height:44px; border-radius:12px; background:#EEF3FA; display:flex; align-items:center; justify-content:center; margin-bottom:16px;">
              {SVG_CLOCK}
            </div>
            <h3 style="font-family:'Recoleta',Georgia,serif; font-size:20px; line-height:1.26 !important; color:#233E85 !important; margin-bottom:10px;">
              Working Hours
            </h3>
            <p style="font-size:14px; line-height:1.6 !important; color:#4A5568 !important; margin-bottom:8px;">
              <strong>Monday &ndash; Friday:</strong><br>
              Morning: 9:30 AM &ndash; 2:00 PM<br>
              Evening: 4:00 PM &ndash; 8:30 PM
            </p>
            <p style="font-size:14px; line-height:1.6 !important; color:#4A5568 !important; margin-bottom:8px;">
              <strong>Saturday:</strong> 9:00 AM &ndash; 5:00 PM
            </p>
            <p style="font-size:13.5px; line-height:1.6 !important; color:#C53030 !important; margin:0;">
              <strong>Sunday:</strong> Holiday (Emergency on Call)
            </p>
          </div>
        </div>

        <!-- CLINIC PHOTO BANNER -->
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:20px; margin-bottom:48px;">
          <div class="photo-card reveal-blur stagger-1">
            <img src="{asset_prefix}images/clinic_entrance.jpg" alt="Clinic Entrance Chromepet" style="width:100%; height:240px; object-fit:cover; display:block;"/>
            <div style="padding:14px 18px; font-size:13px; color:#536B88; font-weight:600;">Main Entrance &bull; No. 9/29C Chromepet</div>
          </div>
          <div class="photo-card reveal-blur stagger-2">
            <img src="{asset_prefix}images/clinic_interior_reception.jpg" alt="Reception Area" style="width:100%; height:240px; object-fit:cover; display:block;"/>
            <div style="padding:14px 18px; font-size:13px; color:#536B88; font-weight:600;">Patient Waiting &bull; Consultation Desk</div>
          </div>
          <div class="photo-card reveal-blur stagger-3">
            <img src="{asset_prefix}images/clinic_treatment_beds.jpg" alt="Treatment Suites" style="width:100%; height:240px; object-fit:cover; display:block;"/>
            <div style="padding:14px 18px; font-size:13px; color:#536B88; font-weight:600;">Therapy Suites &bull; Laser &amp; Electrotherapy</div>
          </div>
        </div>

        <!-- MAP AND INQUIRY FORM -->
        <div class="reveal-blur" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:36px; background:#FFFFFF; border-radius:24px; padding:36px;  border:1px solid #EEF2F4;">
          <!-- FORM -->
          <div>
            <div class="section-kicker">APPOINTMENT REQUEST</div>
            <h2 style="font-family:'Recoleta',Georgia,serif; font-size:26px; line-height:1.24 !important; color:#233E85 !important; margin-bottom:12px;">
              Request a Consultation
            </h2>
            <p style="font-size:14.5px; line-height:1.6 !important; color:#4A5568 !important; margin-bottom:20px;">
              Fill in your details below or send a quick WhatsApp message to confirm an available slot with Dr. Prabhu Rajan.
            </p>
            <form onsubmit="event.preventDefault(); var n=document.getElementById('c_name').value; var p=document.getElementById('c_phone').value; var s=document.getElementById('c_symp').value; var msg='Hello Dr. Prabhu, my name is ' + encodeURIComponent(n) + ' (Phone: ' + encodeURIComponent(p) + '). Condition: ' + encodeURIComponent(s); window.open('https://wa.me/919042612895?text=' + msg, '_blank');" style="display:flex; flex-direction:column; gap:14px;">
              <div>
                <label style="display:block; font-size:13px; font-weight:600; color:#233E85; margin-bottom:6px;">Your Name *</label>
                <input type="text" id="c_name" required placeholder="e.g. Ramesh Kumar" style="width:100%; padding:12px 16px; border:1px solid #CBD5E0; border-radius:10px; font-size:14px; outline:none;"/>
              </div>
              <div>
                <label style="display:block; font-size:13px; font-weight:600; color:#233E85; margin-bottom:6px;">Phone Number *</label>
                <input type="tel" id="c_phone" required placeholder="e.g. 98400 12345" style="width:100%; padding:12px 16px; border:1px solid #CBD5E0; border-radius:10px; font-size:14px; outline:none;"/>
              </div>
              <div>
                <label style="display:block; font-size:13px; font-weight:600; color:#233E85; margin-bottom:6px;">Pain Area / Symptoms *</label>
                <textarea id="c_symp" required rows="3" placeholder="e.g. Severe lower back pain radiating to left leg for 3 weeks..." style="width:100%; padding:12px 16px; border:1px solid #CBD5E0; border-radius:10px; font-size:14px; outline:none; font-family:sans-serif;"></textarea>
              </div>
              <button type="submit" class="btn-whatsapp" style="justify-content:center; padding:14px; font-size:15px; margin-top:8px;">
                {SVG_WHATSAPP} Send Request via WhatsApp
              </button>
            </form>
          </div>

          <!-- MAP EMBED / INFO -->
          <div style="display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div class="section-kicker">EASY ACCESS</div>
              <h3 style="font-family:'Recoleta',Georgia,serif; font-size:24px; line-height:1.26 !important; color:#233E85 !important; margin-bottom:12px;">
                How to reach our Chromepet clinic
              </h3>
              <ul style="padding-left:18px; margin:0 0 20px 0; font-size:14px; line-height:1.7; color:#4A5568;">
                <li><strong>From GST Road / Chromepet Railway Station:</strong> Take Station Road toward New Colony, turn onto 1st Cross Street behind the police station (approx 5 mins).</li>
                <li><strong>From Pallavaram:</strong> Head south along GST Road, cross MIT bridge, take New Colony main entrance.</li>
                <li><strong>Parking:</strong> Dedicated two-wheeler parking and street car parking directly outside the clinic premises.</li>
              </ul>
            </div>
            
            <div style="background:#FAF6EE; border-radius:16px; padding:20px; border:1px solid #E2E8F0;">
              <p style="font-size:14px; font-weight:600; color:#233E85; margin-bottom:10px;">
                {SVG_MAP_PIN} Google Business Verification:
              </p>
              <p style="font-size:13px; line-height:1.5; color:#536B88; margin-bottom:14px;">
                Verified on Google Knowledge Graph (ID: /g/11bvzw43py). Rated 4.9 Stars across 730+ patient reviews on Justdial and 99% Recommended on Practo.
              </p>
              <a href="https://share.google/tpyR96H2jyHYaLHxz" target="_blank" class="btn-primary" style="width:100%; justify-content:center; font-size:13.5px; padding:10px 18px;">
                Open Interactive Directions &rarr;
              </a>
            </div>
          </div>
        </div>

      </div>
    </section>

{get_cta_section(depth_prefix)}
  </main>

{get_global_footer(depth_prefix)}"""


# Generation execution
def build_all():
    print("Building all 9 service pages + contact page...")
    pages_to_build = []

    for s in SERVICES_DATA:
        slug = s["slug"]
        # Root .html
        root_html = render_service_page(s, "")
        # Folder /index.html
        sub_html = render_service_page(s, "../")
        pages_to_build.append((f"{slug}.html", root_html))
        pages_to_build.append((os.path.join(slug, "index.html"), sub_html))

    # Contact page
    contact_root = render_contact_page("")
    contact_sub = render_contact_page("../")
    pages_to_build.append(("contact.html", contact_root))
    pages_to_build.append((os.path.join("contact", "index.html"), contact_sub))

    for rel_path, content in pages_to_build:
        full_path = os.path.join(ROOT_DIR, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {rel_path} ({len(content)} bytes)")

    print(f"Successfully generated {len(pages_to_build)} files (10 pages x 2 dual routing formats)!")


if __name__ == "__main__":
    build_all()
