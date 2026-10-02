<?php
/**
 * Kontaktformular – Versand per PHP mail() (läuft auf jedem Hostinger-Webhosting).
 * Anpassen: $TO und $FROM (die Absenderadresse sollte zu deiner Domain gehören, damit Mails nicht im Spam landen).
 */
declare(strict_types=1);

$TO    = 'hallo@deine-domain.de';
$FROM  = 'formular@deine-domain.de';
$SITE  = 'Mika Reiner – DJ & Videograf';
$MAX_PER_HOUR = 5;   // pro IP

header('X-Robots-Tag: noindex');
$wantsJson = (isset($_SERVER['HTTP_ACCEPT']) && str_contains($_SERVER['HTTP_ACCEPT'], 'application/json'));

function finish(bool $ok, string $msg, bool $json, int $code = 200): void {
    if ($json) {
        http_response_code($ok ? 200 : $code);
        header('Content-Type: application/json; charset=utf-8');
        echo json_encode(['ok' => $ok, 'message' => $msg], JSON_UNESCAPED_UNICODE);
    } else {
        header('Location: /kontakt/?' . ($ok ? 'gesendet=1' : 'fehler=1') . '#formular', true, 303);
    }
    exit;
}
function clean(string $v, int $max = 2000): string {
    $v = trim(str_replace(["\r", "\0"], '', $v));
    return mb_substr($v, 0, $max);
}
function oneLine(string $v, int $max = 200): string {
    return clean(preg_replace('/[\r\n]+/', ' ', $v) ?? '', $max);
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Location: /kontakt/', true, 303);
    exit;
}

// Spam-Schutz: Honeypot + Mindestzeit
if (!empty($_POST['website'])) { finish(true, 'Danke!', $wantsJson); }                 // Bot: stillschweigend "Erfolg"
$ts = (int)($_POST['ts'] ?? 0);
if ($ts > 0 && (time() - $ts) < 3) { finish(false, 'Bitte versuche es in einem Moment erneut.', $wantsJson, 429); }

// Rate-Limit (Dateibasiert, ohne Datenbank)
$ip   = $_SERVER['REMOTE_ADDR'] ?? '0';
$file = sys_get_temp_dir() . '/kontakt_' . md5($ip . date('YmdH')) . '.cnt';
$cnt  = is_file($file) ? (int)file_get_contents($file) : 0;
if ($cnt >= $MAX_PER_HOUR) { finish(false, 'Zu viele Anfragen. Bitte schreib mir direkt per E-Mail.', $wantsJson, 429); }

$labels = [
    'dj-hochzeit' => 'Hochzeits-DJ', 'video-hochzeit' => 'Hochzeitsfilm', 'kombi' => 'DJ + Video (Kombi)',
    'dj-firma' => 'DJ Firmenevent', 'video-firma' => 'Imagefilm / Eventvideo', 'dj-privat' => 'DJ private Feier', 'sonstiges' => 'Sonstiges',
];
$anlass    = (string)($_POST['anlass'] ?? '');
$name      = oneLine((string)($_POST['name'] ?? ''), 120);
$email     = oneLine((string)($_POST['email'] ?? ''), 160);
$tel       = oneLine((string)($_POST['tel'] ?? ''), 40);
$datum     = oneLine((string)($_POST['datum'] ?? ''), 20);
$ort       = oneLine((string)($_POST['ort'] ?? ''), 160);
$gaeste    = oneLine((string)($_POST['gaeste'] ?? ''), 10);
$nachricht = clean((string)($_POST['nachricht'] ?? ''), 4000);

if (!isset($labels[$anlass]) || $name === '' || $nachricht === '' || !filter_var($email, FILTER_VALIDATE_EMAIL) || empty($_POST['datenschutz'])) {
    finish(false, 'Bitte prüfe deine Angaben und versuche es erneut.', $wantsJson, 422);
}

$subject = '=?UTF-8?B?' . base64_encode("Neue Anfrage: {$labels[$anlass]} – $name") . '?=';
$body = "Neue Anfrage über die Website\n\n"
      . "Anlass:   {$labels[$anlass]}\nName:     $name\nE-Mail:   $email\nTelefon:  " . ($tel ?: '–') . "\n"
      . "Datum:    " . ($datum ?: '–') . "\nOrt:      " . ($ort ?: '–') . "\nGäste:    " . ($gaeste ?: '–') . "\n\n"
      . "Nachricht:\n$nachricht\n\n--\nIP: $ip\n";
$headers = [
    'From' => "$SITE <$FROM>", 'Reply-To' => "$name <$email>", 'MIME-Version' => '1.0',
    'Content-Type' => 'text/plain; charset=UTF-8', 'X-Mailer' => 'PHP/' . PHP_VERSION,
];

if (@mail($TO, $subject, $body, $headers)) {
    @file_put_contents($file, (string)($cnt + 1));
    finish(true, 'Danke dir! Deine Anfrage ist angekommen. Ich melde mich innerhalb von 24 Stunden.', $wantsJson);
}
finish(false, 'Das Senden hat leider nicht geklappt. Bitte schreib mir direkt per E-Mail.', $wantsJson, 500);
