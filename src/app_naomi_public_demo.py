"""Demo sintética da Naomi AI para portfólio.

Este arquivo não deriva do núcleo privado. Ele não usa rede, IA, memória,
automação, autenticação ou integrações reais.
"""

from dataclasses import dataclass
from enum import Enum


class DemoRoute(str, Enum):
    INVALID = "entrada_invalida"
    HELP = "ajuda"
    STATUS = "status"
    CONVERSATION = "conversa"


@dataclass(frozen=True)
class DemoResult:
    route: DemoRoute
    message: str


class NaomiPublicDemo:
    """Pipeline local e deliberadamente simples para fins demonstrativos."""

    def process(self, text: str) -> DemoResult:
        normalized = " ".join((text or "").strip().casefold().split())
        if not normalized:
            return DemoResult(DemoRoute.INVALID, "Digite uma mensagem para a demo.")
        if normalized in {"ajuda", "help", "?"}:
            return DemoResult(
                DemoRoute.HELP,
                "Comandos da demo: ajuda, status ou uma mensagem livre.",
            )
        if normalized == "status":
            return DemoResult(
                DemoRoute.STATUS,
                "Demo pública online; nenhum serviço real foi iniciado.",
            )
        return DemoResult(
            DemoRoute.CONVERSATION,
            "Mensagem classificada pela demonstração conceitual.",
        )


def main() -> None:
    demo = NaomiPublicDemo()
    print("Naomi AI — demo pública sintética")
    print("Digite ajuda, status, uma mensagem livre ou sair.\n")
    while True:
        user_input = input("Você: ").strip()
        if user_input.casefold() in {"sair", "exit", "quit"}:
            print("Demo encerrada.")
            return
        result = demo.process(user_input)
        print(f"[{result.route.value}] {result.message}\n")


if __name__ == "__main__":
    main()
