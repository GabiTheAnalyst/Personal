import yahooquery as yq

aapl = yq.Ticker('aapl')
# income_stat = aapl.income_statement()

class STOCK:

    def __init__(self, ticker_id):
        self.ticker = yq.Ticker(ticker_id)
        self.ticker_id = ticker_id

    def balance_sheet(self):
        """
        keys:
        ['asOfDate', 'periodType', 'AccountsPayable', 'AccountsReceivable',
       'AccumulatedDepreciation', 'AllowanceForDoubtfulAccountsReceivable',
       'AvailableForSaleSecurities', 'CapitalStock', 'CashAndCashEquivalents',
       'CashCashEquivalentsAndShortTermInvestments', 'CashEquivalents',
       'CashFinancial', 'CommercialPaper', 'CommonStock', 'CommonStockEquity',
       'CurrentAccruedExpenses', 'CurrentAssets', 'CurrentDebt',
       'CurrentDebtAndCapitalLeaseObligation', 'CurrentDeferredLiabilities',
       'CurrentDeferredRevenue', 'CurrentLiabilities',
       'GainsLossesNotAffectingRetainedEarnings', 'Goodwill',
       'GoodwillAndOtherIntangibleAssets', 'GrossAccountsReceivable',
       'GrossPPE', 'Inventory', 'InvestedCapital',
       'InvestmentinFinancialAssets', 'InvestmentsAndAdvances',
       'LandAndImprovements', 'Leases', 'LongTermDebt',
       'LongTermDebtAndCapitalLeaseObligation', 'MachineryFurnitureEquipment',
       'NetDebt', 'NetPPE', 'NetTangibleAssets',
       'NonCurrentDeferredLiabilities', 'NonCurrentDeferredRevenue',
       'NonCurrentDeferredTaxesLiabilities', 'OrdinarySharesNumber',
       'OtherCurrentAssets', 'OtherCurrentBorrowings',
       'OtherCurrentLiabilities', 'OtherIntangibleAssets',
       'OtherNonCurrentAssets', 'OtherNonCurrentLiabilities',
       'OtherReceivables', 'OtherShortTermInvestments', 'Payables',
       'PayablesAndAccruedExpenses', 'Properties', 'Receivables',
       'RetainedEarnings', 'ShareIssued', 'StockholdersEquity',
       'TangibleBookValue', 'TotalAssets', 'TotalCapitalization', 'TotalDebt',
       'TotalEquityGrossMinorityInterest',
       'TotalLiabilitiesNetMinorityInterest', 'TotalNonCurrentAssets',
       'TotalNonCurrentLiabilitiesNetMinorityInterest',
       'TradeandOtherPayablesNonCurrent', 'WorkingCapital']
        """
        return self.ticker.balance_sheet()

    def cash_flow(self):
        """
        keys:
        ['asOfDate', 'periodType', 'BeginningCashPosition', 'CapitalExpenditure',
       'CashDividendsPaid', 'CashFlowFromContinuingFinancingActivities',
       'ChangeInAccountPayable', 'ChangeInCashSupplementalAsReported',
       'ChangeInInventory', 'ChangeInWorkingCapital',
       'ChangesInAccountReceivables', 'CommonStockIssuance',
       'DeferredIncomeTax', 'DepreciationAndAmortization', 'EndCashPosition',
       'FreeCashFlow', 'InvestingCashFlow', 'NetIncome',
       'NetOtherFinancingCharges', 'NetOtherInvestingChanges',
       'OperatingCashFlow', 'OtherNonCashItems', 'PurchaseOfBusiness',
       'PurchaseOfInvestment', 'RepaymentOfDebt', 'RepurchaseOfCapitalStock',
       'SaleOfInvestment', 'StockBasedCompensation']
        """
        return self.ticker.cash_flow()

    def income_statement(self):
        """
        keys:
        ['asOfDate', 'periodType', 'BasicAverageShares', 'BasicEPS',
       'CostOfRevenue', 'DilutedAverageShares', 'DilutedEPS',
       'DilutedNIAvailtoComStockholders', 'EBIT', 'EBITDA', 'GrossProfit',
       'InterestExpense', 'InterestExpenseNonOperating', 'InterestIncome',
       'InterestIncomeNonOperating', 'NetIncome',
       'NetIncomeCommonStockholders', 'NetIncomeContinuousOperations',
       'NetIncomeFromContinuingAndDiscontinuedOperation',
       'NetIncomeFromContinuingOperationNetMinorityInterest',
       'NetIncomeIncludingNoncontrollingInterests', 'NetInterestIncome',
       'NetNonOperatingInterestIncomeExpense', 'NormalizedEBITDA',
       'NormalizedIncome', 'OperatingExpense', 'OperatingIncome',
       'OperatingRevenue', 'OtherIncomeExpense',
       'OtherNonOperatingIncomeExpenses', 'PretaxIncome',
       'ReconciledCostOfRevenue', 'ReconciledDepreciation',
       'ResearchAndDevelopment', 'SellingGeneralAndAdministration',
       'TaxEffectOfUnusualItems', 'TaxProvision', 'TaxRateForCalcs',
       'TotalExpenses', 'TotalOperatingIncomeAsReported', 'TotalRevenue']
        """
        return self.ticker.income_statement()

    def valuation_measures(self):
        """
        keys:
        ['asOfDate', 'periodType', 'EnterpriseValue',
       'EnterprisesValueEBITDARatio', 'EnterprisesValueRevenueRatio',
       'ForwardPeRatio', 'MarketCap', 'PbRatio', 'PeRatio', 'PegRatio',
       'PsRatio']
        """
        return self.ticker.valuation_measures

    def all_financial_data(self):
        """
        keys:
        ['asOfDate', 'periodType', 'AccountsPayable', 'AccountsReceivable',
       'AccumulatedDepreciation', 'AllowanceForDoubtfulAccountsReceivable',
       'AvailableForSaleSecurities', 'BasicAverageShares', 'BasicEPS',
       'BeginningCashPosition', 'CapitalExpenditure', 'CapitalStock',
       'CashAndCashEquivalents', 'CashCashEquivalentsAndShortTermInvestments',
       'CashDividendsPaid', 'CashEquivalents', 'CashFinancial',
       'CashFlowFromContinuingFinancingActivities', 'ChangeInAccountPayable',
       'ChangeInCashSupplementalAsReported', 'ChangeInInventory',
       'ChangeInWorkingCapital', 'ChangesInAccountReceivables',
       'CommercialPaper', 'CommonStock', 'CommonStockEquity',
       'CommonStockIssuance', 'CostOfRevenue', 'CurrentAccruedExpenses',
       'CurrentAssets', 'CurrentDebt', 'CurrentDebtAndCapitalLeaseObligation',
       'CurrentDeferredLiabilities', 'CurrentDeferredRevenue',
       'CurrentLiabilities', 'DeferredIncomeTax',
       'DepreciationAndAmortization', 'DilutedAverageShares', 'DilutedEPS',
       'DilutedNIAvailtoComStockholders', 'EBIT', 'EndCashPosition',
       'EnterpriseValue', 'EnterprisesValueEBITDARatio',
       'EnterprisesValueRevenueRatio', 'ForwardPeRatio', 'FreeCashFlow',
       'GainsLossesNotAffectingRetainedEarnings', 'Goodwill',
       'GoodwillAndOtherIntangibleAssets', 'GrossAccountsReceivable',
       'GrossPPE', 'GrossProfit', 'InterestExpense',
       'InterestExpenseNonOperating', 'InterestIncome',
       'InterestIncomeNonOperating', 'Inventory', 'InvestedCapital',
       'InvestingCashFlow', 'InvestmentinFinancialAssets',
       'InvestmentsAndAdvances', 'LandAndImprovements', 'Leases',
       'LongTermDebt', 'LongTermDebtAndCapitalLeaseObligation',
       'MachineryFurnitureEquipment', 'MarketCap', 'NetDebt', 'NetIncome',
       'NetIncomeCommonStockholders',
       'NetIncomeContinuousOperations',
       'NetIncomeFromContinuingAndDiscontinuedOperation',
       'NetIncomeFromContinuingOperationNetMinorityInterest',
       'NetIncomeIncludingNoncontrollingInterests', 'NetInterestIncome',
       'NetNonOperatingInterestIncomeExpense', 'NetOtherFinancingCharges',
       'NetOtherInvestingChanges', 'NetPPE', 'NetTangibleAssets',
       'NonCurrentDeferredLiabilities', 'NonCurrentDeferredRevenue',
       'NonCurrentDeferredTaxesLiabilities', 'NormalizedEBITDA',
       'NormalizedIncome', 'OperatingCashFlow', 'OperatingExpense',
       'OperatingIncome', 'OperatingRevenue', 'OrdinarySharesNumber',
       'OtherCurrentAssets', 'OtherCurrentBorrowings',
       'OtherCurrentLiabilities', 'OtherIncomeExpense',
       'OtherIntangibleAssets', 'OtherNonCashItems', 'OtherNonCurrentAssets',
       'OtherNonCurrentLiabilities', 'OtherNonOperatingIncomeExpenses',
       'OtherReceivables', 'OtherShortTermInvestments', 'Payables',
       'PayablesAndAccruedExpenses', 'PbRatio', 'PeRatio', 'PegRatio',
       'PretaxIncome', 'Properties', 'PsRatio', 'PurchaseOfBusiness',
       'PurchaseOfInvestment', 'Receivables', 'ReconciledCostOfRevenue',
       'ReconciledDepreciation', 'RepaymentOfDebt', 'RepurchaseOfCapitalStock',
       'ResearchAndDevelopment', 'RetainedEarnings', 'SaleOfInvestment',
       'SellingGeneralAndAdministration', 'ShareIssued',
       'StockBasedCompensation', 'StockholdersEquity', 'TangibleBookValue',
       'TaxEffectOfUnusualItems', 'TaxProvision', 'TaxRateForCalcs',
       'TotalAssets', 'TotalCapitalization', 'TotalDebt',
       'TotalEquityGrossMinorityInterest', 'TotalExpenses',
       'TotalLiabilitiesNetMinorityInterest', 'TotalNonCurrentAssets',
       'TotalNonCurrentLiabilitiesNetMinorityInterest',
       'TotalOperatingIncomeAsReported', 'TotalRevenue',
       'TradeandOtherPayablesNonCurrent', 'WorkingCapital']
        """
        return self.ticker.all_financial_data()

    def summary_detail(self):
        """
        {'aapl': {'maxAge': 1,
          'priceHint': 2,
          'previousClose': 132.03,
          'open': 133.8,
          'dayLow': 133.59,
          'dayHigh': 136.4,
          'regularMarketPreviousClose': 132.03,
          'regularMarketOpen': 133.8,
          'regularMarketDayLow': 133.59,
          'regularMarketDayHigh': 136.4,
          'dividendRate': 0.82,
          'dividendYield': 0.0062,
          'exDividendDate': '2020-11-06 01:00:00',
          'payoutRatio': 0.24239999,
          'fiveYearAvgDividendYield': 1.46,
          'beta': 1.283613,
          'trailingPE': 41.582317,
          'forwardPE': 31.210527,
          'volume': 77563827,
          'regularMarketVolume': 77563827,
          'averageVolume': 107957417,
          'averageVolume10days': 96812442,
          'averageDailyVolume10Day': 96812442,
          'bid': 136.18,
          'ask': 136.2,
          'bidSize': 1100,
          'askSize': 1100,
          'marketCap': 2294529916928,
          'fiftyTwoWeekLow': 53.1525,
          'fiftyTwoWeekHigh': 138.79,
          'priceToSalesTrailing12Months': 8.358486,
          'fiftyDayAverage': 128.2497,
          'twoHundredDayAverage': 116.33259,
          'trailingAnnualDividendRate': 0.795,
          'trailingAnnualDividendYield': 0.006021359,
          'currency': 'USD',
          'fromCurrency': None,
          'toCurrency': None,
          'lastMarket': None,
          'algorithm': None,
          'tradeable': False}}
        """
        summary_detail = self.ticker.summary_detail

        return summary_detail

    def get_roce(self):
        ebit = self.income_statement()[self.income_statement().periodType == '12M'].iloc[-1]['EBIT']
        total_assets = self.balance_sheet()[self.balance_sheet().periodType == '12M'].iloc[-1]['TotalAssets']
        current_liabilities = self.balance_sheet()[self.balance_sheet().periodType == '12M'].iloc[-1]['CurrentLiabilities']

        roce = ebit / (total_assets - current_liabilities)

        return roce

    def ev_fcf(self):
        ev = self.all_financial_data()['EnterpriseValue'][-1]
        fcf = self.all_financial_data()['FreeCashFlow'][-1]

        return ev / fcf

    def momentum(self):
        price_history_last_year = self.ticker.history(period='1y')['close']
        momentum = (price_history_last_year[-1] / price_history_last_year[0]) - 1

        return momentum

    def beta(self):
        module = 'defaultKeyStatistics'
        values = self.ticker.get_modules(module)
        beta = values[self.ticker_id]['beta']

        return beta

    def dividend_yield(self):
        try:
            dividend_yield = self.summary_detail()[self.ticker_id]['dividendYield']
        except:
            dividend_yield = None

        return dividend_yield


# if __name__== '__main__':
#     stock = STOCK("aapl".lower())
#     beta = stock.beta()

