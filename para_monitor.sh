#!/bin/bash

# Recebe o PID principal do programa Python
PID="$1"

# Solicita o encerramento tratando os erros
kill -TERM "$PID" 2>/dev/null || exit 0

# Aguarda ate 5 segundos pelo encerramento
# e verifica se realmente terminou
for i in 1 2 3 4 5; do
    if ! kill -0 "$PID" 2>/dev/null; then
        break
    fi
    sleep 1
done

exit 0
