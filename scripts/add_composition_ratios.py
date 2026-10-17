from pathlib import Path

path = Path("app/src/main/java/com/frameforge/editor/MainActivity.kt")
source = path.read_text(encoding="utf-8")

if 'import androidx.compose.foundation.layout.aspectRatio' not in source:
    source = source.replace(
        'import androidx.compose.foundation.layout.Arrangement\n',
        'import androidx.compose.foundation.layout.Arrangement\nimport androidx.compose.foundation.layout.aspectRatio\n',
        1,
    )

anchor = '''    Column(
        modifier = Modifier.fillMaxWidth().weight(1f, fill = false).padding(horizontal = 18.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        TextButton(onClick = onBack) { Text("← Voltar aos projetos", color = Accent2) }
        Card(shape = RoundedCornerShape(20.dp), colors = CardDefaults.cardColors(containerColor = Panel)) {
'''
replacement = '''    var selectedRatio by remember(project.id) { mutableStateOf("9:16") }
    val ratioValue = when (selectedRatio) {
        "16:9" -> 16f / 9f
        "1:1" -> 1f
        "4:5" -> 4f / 5f
        "4:3" -> 4f / 3f
        else -> 9f / 16f
    }
    Column(
        modifier = Modifier.fillMaxWidth().weight(1f, fill = false).padding(horizontal = 18.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        TextButton(onClick = onBack) { Text("← Voltar aos projetos", color = Accent2) }
        Card(shape = RoundedCornerShape(20.dp), colors = CardDefaults.cardColors(containerColor = Panel)) {
'''
if 'var selectedRatio by remember(project.id)' not in source:
    if anchor not in source:
        raise SystemExit("Não encontrei o ponto de entrada da tela de projeto; nenhuma alteração foi aplicada.")
    source = source.replace(anchor, replacement, 1)

anchor2 = '''                Divider(color = Color(0xFF303746))
                Text("Este projeto está salvo neste dispositivo.", color = White, fontSize = 14.sp)
'''
replacement2 = '''                Divider(color = Color(0xFF303746))
                Text("Proporção da composição", color = White, fontSize = 15.sp, fontWeight = FontWeight.Bold)
                Text("Escolha o formato de enquadramento para este projeto.", color = Muted, fontSize = 12.sp)
                Row(horizontalArrangement = Arrangement.spacedBy(6.dp), modifier = Modifier.fillMaxWidth()) {
                    listOf("9:16", "16:9", "1:1").forEach { ratio ->
                        if (selectedRatio == ratio) {
                            Button(onClick = { selectedRatio = ratio }, modifier = Modifier.weight(1f), contentPadding = androidx.compose.foundation.layout.PaddingValues(horizontal = 4.dp, vertical = 8.dp)) { Text(ratio, fontSize = 12.sp) }
                        } else {
                            OutlinedButton(onClick = { selectedRatio = ratio }, modifier = Modifier.weight(1f), contentPadding = androidx.compose.foundation.layout.PaddingValues(horizontal = 4.dp, vertical = 8.dp)) { Text(ratio, fontSize = 12.sp) }
                        }
                    }
                }
                Row(horizontalArrangement = Arrangement.spacedBy(6.dp), modifier = Modifier.fillMaxWidth()) {
                    listOf("4:5", "4:3").forEach { ratio ->
                        if (selectedRatio == ratio) {
                            Button(onClick = { selectedRatio = ratio }, modifier = Modifier.weight(1f), contentPadding = androidx.compose.foundation.layout.PaddingValues(horizontal = 4.dp, vertical = 8.dp)) { Text(ratio, fontSize = 12.sp) }
                        } else {
                            OutlinedButton(onClick = { selectedRatio = ratio }, modifier = Modifier.weight(1f), contentPadding = androidx.compose.foundation.layout.PaddingValues(horizontal = 4.dp, vertical = 8.dp)) { Text(ratio, fontSize = 12.sp) }
                        }
                    }
                    Spacer(Modifier.weight(1f))
                }
                Box(modifier = Modifier.fillMaxWidth(), contentAlignment = Alignment.Center) {
                    Box(
                        modifier = Modifier.width(180.dp).aspectRatio(ratioValue)
                            .background(Color(0xFF080A0F), RoundedCornerShape(8.dp)),
                        contentAlignment = Alignment.Center
                    ) {
                        Column(horizontalAlignment = Alignment.CenterHorizontally, verticalArrangement = Arrangement.spacedBy(6.dp)) {
                            Icon(Icons.Default.Movie, contentDescription = null, tint = Accent2, modifier = Modifier.size(27.dp))
                            Text("Prévia " + selectedRatio, color = White, fontSize = 12.sp, fontWeight = FontWeight.SemiBold)
                            Text("Composição vazia", color = Muted, fontSize = 10.sp)
                        }
                    }
                }
                Text("Este projeto está salvo neste dispositivo.", color = White, fontSize = 14.sp)
'''
if 'Text("Proporção da composição"' not in source:
    if anchor2 not in source:
        raise SystemExit("Não encontrei o ponto da descrição do projeto; nenhuma alteração foi aplicada.")
    source = source.replace(anchor2, replacement2, 1)

path.write_text(source, encoding="utf-8")
print("Proporções 9:16, 16:9, 1:1, 4:5 e 4:3 aplicadas.")
