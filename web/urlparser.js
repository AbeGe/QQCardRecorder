var basereplayurl = "replay.html"

function encodeGame(game)
{
	game = game.replace(/����/g, "H");
	game = game.replace(/�¼�/g, "I");
	game = game.replace(/˭�ȴ�/g, "L");
	game = game.replace(/����/g, "M");
	game = game.replace(/ʮ/g, "N");
	game = game.replace(/����/g, "O");
	game = game.replace(/С��/g, "P");
	game = game.replace(/��/g, "R");
	game = game.replace(/÷/g, "S");
	game = game.replace(/��/g, "T");
	game = game.replace(/�ϼ�/g, "U");
	game = game.replace(/��/g, "V");
	game = game.replace(/�Լ�/g, "W");
	game = game.replace(/:/g, "X");
	game = game.replace(/\|/g, "Y");
	game = game.replace(/\n/g, "Z");
	return game;
}

function decodeGame(game)
{
	game = game.replace(/H/g, "����");
	game = game.replace(/I/g, "�¼�");
	game = game.replace(/L/g, "˭�ȴ�");
	game = game.replace(/M/g, "����");
	game = game.replace(/N/g, "ʮ");
	game = game.replace(/O/g, "����");
	game = game.replace(/P/g, "С��");
	game = game.replace(/R/g, "��");
	game = game.replace(/S/g, "÷");
	game = game.replace(/T/g, "��");
	game = game.replace(/U/g, "�ϼ�");
	game = game.replace(/V/g, "��");
	game = game.replace(/W/g, "�Լ�");
	game = game.replace(/X/g, ":");
	game = game.replace(/Y/g, "|");
	game = game.replace(/Z/g, "\n");
	return game;
}


function fetchOriginalGameFromUrl()
{
	obj = {};
	querystring = location.search.substr(1); // those after charactor '?'
	arr = querystring.split('&');
	for (i in arr)
	{
		brr = arr[i].split('=');
		if (brr[0] == "ver") {obj["ver"] = brr[1];}
		if (brr[0] == "game") {obj["game"] = brr[1];}
	}

	return obj;
}

function fetchDecodedGameFromUrl()
{
	obj = fetchOriginalGameFromUrl();
	if (obj["ver"] == 1)
	{
		if (obj["game"] !== undefined) return decodeGame(obj["game"]);
	}
	return false;
}

function generateEncodedGameUrlParam(base, game)
{
	return base + "?ver=1&game="+encodeGame(game);
}

function generateRedirectUrlForReplay(game)
{
	return generateEncodedGameUrlParam(basereplayurl, game)
}
