#!/usr/bin/env python3
"""Genera la portada del repo (estilo lofi hip-hop) -> docs/img/portada.png

Bosque de pinos al atardecer; los pinos rojizos son los muertos por el
escarabajo, y la grilla hexagonal brillante es el autómata celular.

    python docs/img/generar_portada.py
"""

import math
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1280, 640          # proporción 2:1 (social preview de GitHub)
S = 2                     # supermuestreo para suavizar bordes
w, h = W * S, H * S
rng = np.random.default_rng(42)
AQUI = os.path.dirname(os.path.abspath(__file__))
FUENTES = "/usr/share/fonts/truetype/google-fonts"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


def hexrgb(c):
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def degradado(paradas):
    """Degradado vertical a partir de [(posición 0..1, '#color'), ...]."""
    y = np.linspace(0, 1, h)[:, None]
    img = np.zeros((h, w, 3))
    for k in range(3):
        xs = [p for p, _ in paradas]
        ys = [hexrgb(c)[k] for _, c in paradas]
        img[:, :, k] = np.interp(y, xs, ys)
    return Image.fromarray(img.astype(np.uint8)).convert("RGBA")


def pino(draw, x, base, alto, color):
    """Pino estilizado: tronco + pisos de triángulos."""
    ancho = alto * 0.42
    draw.rectangle([x - alto * 0.025, base - alto * 0.12, x + alto * 0.025, base], fill=color)
    pisos = 4
    for k in range(pisos):
        f = k / pisos
        y0 = base - alto * (0.12 + 0.88 * f * 0.85)
        a = ancho * (1 - 0.7 * f)
        draw.polygon([(x - a / 2, y0), (x + a / 2, y0), (x, y0 - alto * 0.42)], fill=color)


def capa_montes(base_y, amp, color, semilla, frec=3):
    r = np.random.default_rng(semilla)
    xs = np.linspace(0, 1, 400)
    ys = base_y + sum(amp / (i + 1) * np.sin(2 * math.pi * (frec * (i + 1) * xs + r.random()))
                      for i in range(4))
    capa = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(capa).polygon([(0, h)] + [(x * w, y * h) for x, y in zip(xs, ys)] + [(w, h)],
                                 fill=color)
    return capa


def main():
    # --- Cielo ---------------------------------------------------------------
    img = degradado([(0.0, "#140f2e"), (0.35, "#3a2465"), (0.62, "#a4508b"),
                     (0.78, "#f08a7b"), (0.9, "#ffc48a"), (1.0, "#ffc48a")])

    # Estrellas
    estrellas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(estrellas)
    for _ in range(260):
        x, y = rng.uniform(0, w), rng.uniform(0, h * 0.5)
        r = rng.choice([1.2, 1.8, 2.6]) * S
        a = int(rng.uniform(60, 220) * (1 - y / (h * 0.5)))
        d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 240, 230, a))
    img = Image.alpha_composite(img, estrellas)

    # Sol con franjas (y su resplandor)
    cx, cy, R = w * 0.73, h * 0.6, h * 0.24
    brillo = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(brillo).ellipse([cx - R * 1.6, cy - R * 1.6, cx + R * 1.6, cy + R * 1.6],
                                   fill=(255, 170, 120, 90))
    img = Image.alpha_composite(img, brillo.filter(ImageFilter.GaussianBlur(70 * S)))
    sol = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ds = ImageDraw.Draw(sol)
    for yy in range(int(cy - R), int(cy + R)):
        t = (yy - (cy - R)) / (2 * R)
        col = tuple(int(a + (b - a) * t) for a, b in zip(hexrgb("#ffe3a3"), hexrgb("#ff7a8a")))
        dx = math.sqrt(max(R * R - (yy - cy) ** 2, 0))
        ds.line([(cx - dx, yy), (cx + dx, yy)], fill=col + (255,))
    for k in range(7):                       # franjas recortadas en la mitad inferior
        y0 = cy + R * (0.12 + 0.13 * k)
        ds.rectangle([cx - R, y0, cx + R, y0 + (2 + k * 1.6) * S], fill=(0, 0, 0, 0))
    img = Image.alpha_composite(img, sol)

    # --- Montañas ------------------------------------------------------------
    img = Image.alpha_composite(img, capa_montes(0.66, 0.035, (120, 62, 122, 255), 1))
    img = Image.alpha_composite(img, capa_montes(0.71, 0.03, (84, 44, 99, 255), 2, frec=2))

    # --- Grilla hexagonal (el autómata) --------------------------------------
    lado = 15 * S
    hx, hy = 1.5 * lado, math.sqrt(3) * lado
    cols, filas = int(w / hx) + 2, int(h * 0.62 / hy) + 2
    foco = (w * 0.47, h * 0.55)
    dens = np.zeros((filas, cols))
    for j in range(cols):                     # mancha orgánica: distancia + ruido
        for i in range(filas):
            x, y = j * hx, i * hy + (hy / 2 if j % 2 else 0)
            dist = math.hypot((x - foco[0]) / (w * 0.22), (y - foco[1]) / (h * 0.2))
            ruido = rng.normal(0, 0.18) + 0.25 * math.sin(x / (90 * S)) * math.cos(y / (70 * S))
            dens[i, j] = np.clip(1.05 - dist + ruido, 0, 1)
    lineas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    celdas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    dl, dc = ImageDraw.Draw(lineas), ImageDraw.Draw(celdas)
    for j in range(cols):
        for i in range(filas):
            x, y = j * hx, i * hy + (hy / 2 if j % 2 else 0)
            pts = [(x + lado * math.cos(math.radians(a)), y + lado * math.sin(math.radians(a)))
                   for a in range(0, 360, 60)]
            fade = max(0.0, 1 - abs(x - w * 0.5) / (w * 0.55)) * min(1, y / (h * 0.15))
            dl.polygon(pts, outline=(255, 220, 240, int(28 * fade)), width=S)
            v = dens[i, j]
            if v > 0.15:
                col = tuple(int(a + (b - a) * v) for a, b in zip(hexrgb("#ff9a76"), hexrgb("#ff4d6d")))
                pts_in = [(x + (px - x) * 0.82, y + (py - y) * 0.82) for px, py in pts]
                dc.polygon(pts_in, fill=col + (int(150 * v * fade),))
    img = Image.alpha_composite(img, lineas)
    img = Image.alpha_composite(img, celdas.filter(ImageFilter.GaussianBlur(9 * S)))
    img = Image.alpha_composite(img, celdas)

    # --- Bosque (3 capas; los rojizos son pinos muertos por el escarabajo) -------
    capas = [(0.80, 95, (52, 30, 72), 0.35), (0.88, 135, (32, 18, 48), 0.5), (0.99, 190, (16, 9, 26), 0.0)]
    for base_rel, alto_px, color, prob_rojo in capas:
        capa = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        dp = ImageDraw.Draw(capa)
        base = h * base_rel
        dp.rectangle([0, base - 4 * S, w, h], fill=color + (255,))
        x = -20 * S
        while x < w + 40 * S:
            alto = alto_px * S * rng.uniform(0.7, 1.25)
            cerca = abs(x - foco[0]) < w * 0.3
            if prob_rojo and cerca and rng.random() < prob_rojo:
                c = (176, 74, 60) if base_rel < 0.85 else (122, 44, 44)
            else:
                c = color
            pino(dp, x, base + rng.uniform(0, 10) * S, alto, c + (255,))
            x += alto * rng.uniform(0.22, 0.36)
        img = Image.alpha_composite(img, capa)

    # --- Texto -----------------------------------------------------------------
    txt = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    dt = ImageDraw.Draw(txt)
    f_mini = ImageFont.truetype(MONO, 22 * S)
    f_tit = ImageFont.truetype(os.path.join(FUENTES, "Poppins-Bold.ttf"), 70 * S)
    f_sub = ImageFont.truetype(os.path.join(FUENTES, "Poppins-Light.ttf"), 30 * S)
    f_tag = ImageFont.truetype(MONO, 19 * S)
    x0, y0 = 64 * S, 70 * S
    dt.text((x0, y0), "lofi beats to parallelize to", font=f_mini, fill=(255, 214, 196, 200))
    dt.text((x0 - 3 * S, y0 + 34 * S), "mountain pine beetle", font=f_tit, fill=(255, 241, 230, 255))
    dt.text((x0, y0 + 128 * S), "a multiscale stochastic cellular automaton",
            font=f_sub, fill=(255, 205, 200, 235))
    tags = ["numba", "mpi", "halo exchange", "bsp"]
    tx = x0
    for t in tags:                            # "píldoras" para las etiquetas
        bw = dt.textlength(t, font=f_tag) + 26 * S
        dt.rounded_rectangle([tx, y0 + 186 * S, tx + bw, y0 + 220 * S], radius=17 * S,
                             outline=(255, 205, 200, 170), width=S)
        dt.text((tx + 13 * S, y0 + 192 * S), t, font=f_tag, fill=(255, 225, 215, 230))
        tx += bw + 12 * S
    sombra = txt.copy().filter(ImageFilter.GaussianBlur(6 * S))
    negro = Image.new("RGBA", (w, h), (20, 8, 30, 0))
    negro.putalpha(sombra.getchannel("A").point(lambda a: int(a * 0.6)))
    img = Image.alpha_composite(img, negro)
    img = Image.alpha_composite(img, txt)

    # --- Acabado lofi: reducir, grano, viñeta y leve desaturación ---------------
    img = img.convert("RGB").resize((W, H), Image.LANCZOS)
    a = np.asarray(img).astype(np.float32)
    a += rng.normal(0, 7, (H, W, 1))                       # grano de película
    yy, xx = np.mgrid[0:H, 0:W]
    vin = 1 - 0.38 * (((xx - W / 2) / (W / 1.6)) ** 2 + ((yy - H / 2) / (H / 1.3)) ** 2)
    a *= np.clip(vin, 0.55, 1)[:, :, None]
    gris = a.mean(axis=2, keepdims=True)
    a = 0.88 * a + 0.12 * gris + np.array([6, 0, 10])      # tono lavado y frío en sombras
    Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(os.path.join(AQUI, "portada.png"))
    print("Guardado en", os.path.join(AQUI, "portada.png"))


if __name__ == "__main__":
    main()
