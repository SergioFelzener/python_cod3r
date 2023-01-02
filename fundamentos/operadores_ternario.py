# operadores ternários

esta_chovendo = True

print("hoje estou com as roupas " + ('secas.', 'molhadas.')[esta_chovendo])

print("hoje estou com as roupas " + ('molhadas.' if esta_chovendo else 'secas.'))
