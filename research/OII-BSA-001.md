# OII-BSA-001 — Broadcast Signal Anomaly Analysis

Date: 2026-11-26. Status: preliminary, open investigation. Method: RABE.

## Question
Identify the audiovisual signal reportedly interrupting the Thanksgiving Bears–Lions broadcast, and distinguish signal identity from the cause of its appearance.

## Evidence
User-supplied 76.045 s social-media MP4, SHA-256 `df25d8bfcd01833cc2630fb368165008d5a3e8eac25754bd7a968271ca2c4879`. Source media not redistributed; original broadcast provenance unverified. Supplied screenshots show magenta/dark fields and NY TX TEST. Visual resemblance to an SDI pathological checkfield is a provisional identification; TX may mean transmission. Neither establishes cause.

## Reproduction
Decode with `ffmpeg -i input.mp4 -vn -ac 1 -ar 48000 -f f32le audio.raw`. Read float32 samples with NumPy. For each one-second interval starting at integer second i, multiply 48000 samples by np.hanning(48000), compute abs(np.fft.rfft(window)), use scipy.signal.find_peaks and sort peaks by amplitude. Bin spacing 1 Hz. Results independently rerun in current session:

| Start (s) | Three or four strongest peaks (Hz), descending amplitude |
|---|---|
|1|1000,1600,199|
|2|1000,1600,200|
|3|1000,1600,200|
|5|1000,1600,200|
|8|1000,1600,586,200|

Approximate 1:5:8 ratio is compatible with harmonics of 200 Hz but does not prove common origin, encoding, or intent. Social media processing, microphone and speaker distortion remain uncontrolled.

## Competing hypotheses
H01 ordinary engineering test feed inadvertently aired; H02 specialized audio diagnostic; H03 equipment harmonic/intermodulation distortion; H04 recording/editing artifacts; H05 routing/switching error; H06 deliberate nonstandard insertion (no affirmative evidence). Hypotheses may overlap. No connection to other incidents established.

## Gates
G01 local spectral reproduction: PASS, limited to supplied clip. G02 independent viewer recordings and provenance: pending. G03 authoritative standards comparison (SMPTE checkfield, audio test configurations, EAS): pending. G04 time-frequency and nonlinear distortion analysis, including phase, amplitude and clipping: pending. G05 historical baseline and provider/geographic scope: pending. G06 broadcaster engineering explanation and independent review: pending. G07 publish reproducible derived results and negative findings after rights/privacy review: pending. Compare independent recordings before attributing tones to broadcast source; do not infer coordination from temporal proximity. No raw third-party footage or identifying viewer information published.

## Conclusion
The measured clip contains stable 1000 and 1600 Hz peaks and a near-200 Hz component. Exact audio configuration and incident cause remain unknown. Preserve alternative explanations and revise as evidence warrants.
