from robo import *
import unittest

class TestInformacoes(unittest.TestCase):
    def setUp(self):
        self.robo = iniciar()

    def test_01_o_que_faz(self):
        perguntas = [
            "O que faz um contador?"
        ]

        for pergunta in perguntas:
            print(f"testando pergunta: {pergunta}")

            resposta = self.robo.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A função do contador é executar tarefas das áreas econômicas,", 
                resposta.text
            )

    def test_02_preciso_de_um_contado(self):
        perguntas = [
            "Porque preciso de um contador?"
        ]

        for pergunta in perguntas:
            print(f"testando pergunta: {pergunta}")

            resposta = self.robo.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Todo o negócio precisa ter a consultoria contábil",
                resposta.text
            )
    
    def test_03_mei(self):
        perguntas = [
            "Oque e um mei?"
        ]

        for pergunta in perguntas:
            print(f"testando pergunta: {pergunta}")

            resposta = self.robo.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O Microempreendedor Individual (MEI) é uma figura jurídica do Brasil",
                resposta.text
            )

    def test_04_dma(self):
        perguntas = [
            "oque e uma DMA?"
        ]

        for pergunta in perguntas:
            print(f"testando pergunta: {pergunta}")

            resposta = self.robo.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A Declaração e Apuração Mensal do imposto",
                resposta.text
            )

    def test_05_irrf(self):
        perguntas = [
            "como é cobrado o irrf?"
        ]

        for pergunta in perguntas:
            print(f"testando pergunta: {pergunta}")

            resposta = self.robo.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Para calcular o IRRF em 2022,",
                resposta.text
            )

    def test_06_fgts(self):
        perguntas = [
            "como é tributado o fgts?"
        ]

        for pergunta in perguntas:
            print(f"testando pergunta: {pergunta}")

            resposta = self.robo.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Os saques do FGTS são rendimentos isentos da cobrança de imposto de renda",
                resposta.text
            )

    def test_07_salario_2023(self):
        perguntas = [
            "qual salario minimo 2023?"
        ]

        for pergunta in perguntas:
            print(f"testando pergunta: {pergunta}")

            resposta = self.robo.get_response(pergunta.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Em 2022, o valor do salário mínimo está em R$ 1.212",
                resposta.text
            )


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TestInformacoes))

    exec = unittest.TextTestRunner()
    exec.run(testes)