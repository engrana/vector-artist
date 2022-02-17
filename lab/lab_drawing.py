from cairo import SVGSurface, Context, SVGUnit


def draw_white_canvas(path, w, h) -> SVGSurface:
    surface = SVGSurface(path, w, h)
    surface.set_document_unit(SVGUnit.USER)
    ctx = Context(surface)
    ctx.scale(w, h)
    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(0, 0, w, h)
    ctx.fill()
    return surface


def draw_line(canvas: SVGSurface, start, end, color, border):
    ctx = Context(canvas)
    ctx.scale(354, 525)
    (r, g, b) = color
    r /= 255
    g /= 255
    b /= 255
    ctx.set_source_rgb(r, g, b)
    ctx.set_line_width(border)
    (x1, y1) = start
    ctx.move_to(x1, y1)
    (x2, y2) = end
    ctx.line_to(x2, y2)
    ctx.close_path()
    ctx.stroke()


if __name__ == '__main__':
    drawing = draw_white_canvas("./resources/images/output/drawing.svg", 354, 525)
    draw_line(drawing, (0.1, 0.1), (0.9, 0.9), (5, 6, 255), 0.05)
    draw_line(drawing, (0.9, 0.1), (0.1, 0.9), (255, 5, 0), 0.05)
    drawing.flush()
    drawing.write_to_png("./resources/images/output/drawing.png")
