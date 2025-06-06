from __future__ import annotations

from dataclasses import KW_ONLY, field
import typing as t

import rio
from authentication.components import news_article
from ... import components as comps

@rio.page(
    name="Home",
    url_segment="home",
)
class HomePage(rio.Component):
    """
    A sample page, containing a greeting and some testimonials.
    """

    def build(self) -> rio.Component:
        return rio.Column(
            news_article.NewsArticle(markdown="ok"),
            rio.Markdown(
                """
# Buzzwordz Inc.!

Unleashing everything in Mehre-pars!!!!!!!! Yes yes yes yes yes
            """,
                min_width=60,
                align_x=0.5,
            ),
            rio.Markdown(
                """
# Buzzwordz Inc.!

Unleashing everything in Mehre-pars!!!!!!!! Yes
            """,
                min_width=60,
                align_x=0.5,
            ),
            rio.Row(
                comps.Testimonial(
                    "Disruptive Innovations Inc. is the vanguard of operational excellence and groundbreaking innovation.",
                    "Jane Doe",
                    "CTO, Synergistic Solutions LLC",
                ),
                comps.Testimonial(
                    "They blew my socks off, and I wasn't even wearing any!",
                    "Made Up Rick",
                    "CEO, Imaginary Industries",
                ),
                comps.Testimonial(
                    "The Quantum Synergy Paradigm is a game-changer! I've never seen anything like it.",
                    "John Doe",
                    "CEO, HyperTech Corp.",
                ),
                spacing=2,
                align_x=0.5,
            ),
            rio.Markdown(
                """
Contact us today to unlock your business's quantum potential and embark on a
journey of transformational growth and stratoasdspheric success.!!!!!
            """,
                min_width=60,
                align_x=0.5,
            ),
            spacing=2,
            min_width=60,
            align_x=0.5,
            align_y=0,
        )

