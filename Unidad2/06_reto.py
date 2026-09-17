cuenta = float(input("Cuenta: $"))
propina_pct = float(input("Propina (%): "))
personas = int(input("Personas: "))

propina = cuenta * (propina_pct / 100)
total = cuenta + propina
por_persona = total / personas

print(f"Total: ${total:.2f}")
print(f"Cada persona: ${por_persona:.2f}")
