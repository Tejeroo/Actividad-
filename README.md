# Laboratorio DevSecOps — Integración IT–OT (simulada)

## Propósito
Convertir requisitos de seguridad en pruebas y controles automáticos de CI.
Este proyecto **no se conecta a PLC, historian, redes OT ni nube real**.

## Requisitos
Python 3.10+; Git; cuenta GitHub para CI.

## Ejecutar localmente
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python -m bandit -r src -q
```

## Ejercicio de regresión
1. Abrir `src/telemetry.py`.
2. Cambiar `return operation == "read"` por `return operation in ("read", "write")`.
3. Ejecutar `python -m pytest -q`. Deben fallar pruebas de seguridad.
4. Restaurar la línea original y volver a ejecutar las pruebas.

## Ejecutar GitHub Actions
1. Crear repositorio **privado** vacío en GitHub (sin README).
2. En la carpeta del proyecto: `git init`, `git add .`, `git commit -m "Initial CI"`, `git branch -M main`.
3. `git remote add origin URL_DE_TU_REPOSITORIO` y `git push -u origin main`.
4. En GitHub abrir pestaña Actions y revisar workflow `CI - pruebas y seguridad`.
5. Crear una rama `git switch -c feature/regresion`, introducir la regresión, hacer commit y push; abrir PR a main y observar el check fallido.
6. Restaurar código, commit, push; verificar check exitoso.

**Importante:** un check fallido no bloquea por sí mismo el merge; se requieren reglas de protección de rama compatibles con el repositorio. Tampoco implica autorización para desplegar a OT.

## Entregable
Diagrama del pipeline; captura de ejecución correcta y fallida; requisito de seguridad asociado; qué verifica el pipeline y qué NO verifica.

## Extensión
Investigar secret scanning, SCA y SBOM; proponer un control adicional adecuado al componente real del proyecto.
