<!DOCTYPE html>
<html lang='fr'>

<head>
    <meta charset="utf-8">
    <title>les données saisies avec succès</title>
</head>

<body>
	<h1>Vos données sont enregistrées!</h1>
    <h3>Retourner pour faire remplir un autre formulaire.</h3>
    <h3>(Penser à sauvergarder le fichier .json sinon la nouvelle entrée va couvrir l'ancienne)</h3>
	<?php
		$json_data = json_encode($_POST);
        file_put_contents('./config.json', $json_data);
	?>
</body>
</html>