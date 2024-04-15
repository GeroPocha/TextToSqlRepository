system_prompts = {
    'Zero-Shot': {
        'name': 'Zero-Shot',
        'prompt': """
            Benutze folgende Datenbank als Grundlage: 'UnternehmenDB' mit den Tabellen 'Lieferanten', 'Produkte', 'Umsaetze' und 'Vertraege'.
            - 'Lieferanten' enthält 'LieferantenID', 'Name', 'Adresse', 'Ansprechpartner', 'Bewertung'.
            - 'Produkte' enthält 'ProduktID', 'ProduktName', 'Beschreibung', 'Standard-Preis', 'Kategorie', 'Lagerbestand', 'LieferantenID'.
            - 'Umsaetze' enthält 'UmsatzID', 'ProduktID', 'LieferantenID', 'Datum', 'Ver-kaufteMenge', 'Preis', 'Verkaufskanal'.
            - 'Vertraege' enthält 'VertragID', 'LieferantenID', 'Vertragsbeginn', 'Ver-tragsende', 'Vertragsbedingungen', 'Status', 'Vertragswert'.

            Dir wird nun in natürlicher Sprache eine Aufgabe geben, du musst basierend auf der UnternehmenDB aus der Eingabe eine Query mit gültiger SQL Syntax machen. Gib nichts außer der Query aus.
            """
    },
    'One-Shot': {
        'name': 'One-Shot',
        'prompt': """
            Benutze folgende Datenbank als Grundlage: 'UnternehmenDB' mit den Tabellen 'Lieferanten', 'Produkte', 'Umsaetze' und 'Vertraege'.
            - 'Lieferanten' enthält 'LieferantenID', 'Name', 'Adresse', 'Ansprechpartner', 'Bewertung'.
            - 'Produkte' enthält 'ProduktID', 'ProduktName', 'Beschreibung', 'Standard-Preis', 'Kategorie', 'Lagerbestand', 'LieferantenID'.
            - 'Umsaetze' enthält 'UmsatzID', 'ProduktID', 'LieferantenID', 'Datum', 'Ver-kaufteMenge', 'Preis', 'Verkaufskanal'.
            - 'Vertraege' enthält 'VertragID', 'LieferantenID', 'Vertragsbeginn', 'Ver-tragsende', 'Vertragsbedingungen', 'Status', 'Vertragswert'.

            Dir wird nun in natürlicher Sprache eine Aufgabe geben, du musst basierend auf der UnternehmenDB aus der Eingabe eine Query mit gültiger SQL Syntax machen. Gib nichts außer der Query aus.
            Beispiel:
            Wenn der Nutzer fragt: "Zeige mir alle Produkte in der Kategorie 'Elektronik', die einen Lagerbestand unter 50 haben.", dann lautet die SQL-Abfrage: "SELECT * FROM Produkte WHERE Kategorie = 'Elektronik' AND Lagerbestand < 50;".
            """
    },
    'Role Prompting': {
        'name': 'Role Prompting',
        'prompt': """
            Als Datenbankexperte für 'UnternehmenDB', spezialisiert auf die Analyse und Verwaltung der Tabellen 'Lieferanten', 'Produkte', 'Umsaetze', und 'Vertraege', ist es deine Aufgabe, datengetriebene Lösungen zu finden. 
            Dein tiefgehendes Verständnis der Datenbankstruktur ermöglicht es dir, komplexe Abfragen effizient zu konstruieren.
            Benutze folgende Datenbank als Grundlage: 'UnternehmenDB' mit den Tabellen 'Lieferanten', 'Produkte', 'Umsaetze' und 'Vertraege'.
            - 'Lieferanten' enthält 'LieferantenID', 'Name', 'Adresse', 'Ansprechpartner', 'Bewertung'.
            - 'Produkte' enthält 'ProduktID', 'ProduktName', 'Beschreibung', 'Standard-Preis', 'Kategorie', 'Lagerbestand', 'LieferantenID'.
            - 'Umsaetze' enthält 'UmsatzID', 'ProduktID', 'LieferantenID', 'Datum', 'Ver-kaufteMenge', 'Preis', 'Verkaufskanal'.
            - 'Vertraege' enthält 'VertragID', 'LieferantenID', 'Vertragsbeginn', 'Ver-tragsende', 'Vertragsbedingungen', 'Status', 'Vertragswert'.

            Dir wird nun in natürlicher Sprache eine Aufgabe geben, du musst basierend auf der UnternehmenDB aus der Eingabe eine Query mit gültiger SQL Syntax machen. Gib nichts außer der Query aus.
           """
    },
    'Chain of Thought': {
        'name': 'Chain of Thought',
        'prompt': """
            Benutze folgende Datenbank als Grundlage: 'UnternehmenDB' mit den Tabellen 'Lieferanten', 'Produkte', 'Umsaetze' und 'Vertraege'.
            - 'Lieferanten' enthält 'LieferantenID', 'Name', 'Adresse', 'Ansprechpartner', 'Bewertung'.
            - 'Produkte' enthält 'ProduktID', 'ProduktName', 'Beschreibung', 'Standard-Preis', 'Kategorie', 'Lagerbestand', 'LieferantenID'.
            - 'Umsaetze' enthält 'UmsatzID', 'ProduktID', 'LieferantenID', 'Datum', 'Ver-kaufteMenge', 'Preis', 'Verkaufskanal'.
            - 'Vertraege' enthält 'VertragID', 'LieferantenID', 'Vertragsbeginn', 'Ver-tragsende', 'Vertragsbedingungen', 'Status', 'Vertragswert'.

            Dir wird nun in natürlicher Sprache eine Aufgabe geben, du musst basierend auf der UnternehmenDB aus der Eingabe eine Query mit gültiger SQL Syntax machen. Gib nichts außer der Query aus.
           
            Um eine SQL-Abfrage basierend auf einer natürlichsprachlichen Anfrage zu gene-rieren, gehe wie folgt vor:
            1. Identifiziere, welche Informationen gesucht sind. Bestimme die Felder, die aus der Datenbank selektiert werden sollen.
            2. Ermittle, aus welchen Tabellen diese Felder bezogen werden können. Berück-sichtige dabei die Struktur der 'UnternehmenDB' und die Beziehungen zwischen den Tabellen 'Lieferanten', 'Produkte', 'Umsaetze' und 'Vertraege'.
            3. Prüfe, unter welchen Bedingungen die Informationen selektiert werden sol-len. Identifiziere die Kriterien für die Filterung der Daten und wie diese Kriterien auf die Felder und Tabellen angewendet werden.
            4. Überlege, ob und wie die Daten aus verschiedenen Tabellen miteinander ver-knüpft werden müssen, um die gesuchten Informationen zu erhalten. Dies kann den Einsatz von JOIN-Operationen oder die Kombination von mehreren Abfragen beinhalten.
            5. Formuliere die SQL-Abfrage, indem du die identifizierten Felder selek-tierst, die entsprechenden Tabellen ansprichst, die festgelegten Bedingungen anwendest und die notwendigen Verknüpfungen zwischen den Tabellen herstellst.
           """
    },
}

user_prompts = [
    'Nenn mir die Namen aller Lieferanten mit einer Bewertung von mindestens vier.',
    'Wie viele unserer Lieferanten sitzen in Deutschland?.',
    'Was für eine Bewertung hat die Proteinshake GmbH?',
    'Wie heißt unser Ansprechpartner bei der leckere Pizza AG?',
    'Aus welchem Land kommt unser schlecht bewertester Lieferant?',
    'Wie viele Verträge zwischen uns und der koffeinCola GmbH laufen dieses Jahr aus?',
    'Was ist die Adresse von dem Lieferanten bei dem wir das Produkt mit dem höchsten Standardpreis beziehen?',
    'Bei welchem Lieferanten beziehen wir den Artikel mit der ID 7?',
    'Was ist die Bewertung von dem Lieferanten, mit dem wir schon am längsten zusammen arbeiten?',
    'Wie viele Produkte beziehen wir von der GehtSchnellKaputt GmbH?',
    "Wie viele Verträge sind zum Stichtag 31.05.2024 aktiv mit dem Lieferanten, der uns die meisten Produkte in der Kategorie 'Non Food' liefert?",
    'Was für einen Umsatz haben wir am 20.02.2024 mit allen Produkten von dem Lieferanten mit dem wir den Vertrag mit dem höchsten Vertragwert haben?',
    'Wie viel Lieferanten haben wir mit einer Bewertung von mindestens 3, mit deren Produkte wir schonmal an einem Tag über 5000€ im Online Verkauf verdient haben?',
    'Was ist der Vertragswert des wertvollsten Vertrages den wir mit dem Lieferanten haben, der am 03.03.2024 den größten Umsatz gebracht hat?',
    'Wie heißt das Produkt mit dem niedrigsten Standardpreis, von dem Lieferanten der die meisten Verträge mit uns hat, die am 12.12.2024 enden?'
]

loesungen = [
    'Süße Bonbons GmbH Langweilige Salate leckere Pizza AG GehtSchnellKaputt GmbH Proteinshake GmbH nullnummer Zero Getränke UG',
    '6',
    '5',
    'Felix Tomatensauce',
    "Italien",
    '3',
    'Via Capannori 43 Rom Italien',
    'nullnummer Zero Getränke UG',
    '5',
    '12',
    "6",
    '825',
    '3',
    '140000',
    'Teller aus Papier'
]