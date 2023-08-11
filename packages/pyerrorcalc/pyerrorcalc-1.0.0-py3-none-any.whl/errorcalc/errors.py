from latex_containers import Latex_Container, Math, Equation
from sympy import latex,simplify,sqrt,Symbol,Expr

def product(iterable:set, repeat:int) -> tuple:
    for combination in _product_helper(iterable,repeat):
        yield combination

def _product_helper(iterable,n,combination=tuple()):
    if n==0:
        yield combination
    else:
        for item in iterable:
            yield from _product_helper(iterable,n-1,(*combination,item))


class gauss:
    _eq_symbol = 'G'
    _title = "Fehlerbestimmung mit der Gauß-Fehlerfortpflanzungsformel"
    
    def __init__(self, expr: Expr, values:dict = {}, eq_symbol:str = _eq_symbol, title:str = _title):
        self.title = title
        self.eq_symbol = eq_symbol

        self.expr = expr
        self.deltas = {sym : Symbol(f"\\Delta {latex(sym)}") for sym in self.expr.free_symbols}
        self.values = dict(values)
        
        for sym,tup in dict(self.values).items():
            self.values[self.deltas[sym]] = tup[1]
            self.values[sym] = tup[0]

        self.partials = {sym : simplify(self.expr.diff(sym)) for sym in self.deltas.keys()}

        self.value = self.expr.evalf(subs=self.values)
        self.gauss_expr = simplify(sqrt(sum([(self.deltas[sym] * self.partials[sym])**2 for sym in self.deltas.keys()])))
        self.gauss_delta = self.gauss_expr.evalf(subs=self.values) if self.values else 0

    def latex(self, verbose:bool = False) -> str:
        c = Latex_Container()
        
        c.add(Equation(f"{self.eq_symbol} = {latex(self.expr)}"))
        
        if self.values:
            m = Math()
            for sym in self.expr.free_symbols:
                s = f"{latex(sym)} = {self.values[sym]}"
                error = self.values[self.deltas[sym]]
                if error:
                    s += f" \\pm {error}"
                m.add(s)
            c.add(m)
        
        m = Math()
        for sym,partial in self.partials.items():
            s = "\\frac{\\partial %s}{\\partial %s} = %s" % (self.eq_symbol, latex(sym), latex(partial))
            if self.values:
                s += f" = {partial.evalf(subs=self.values)}"
            m.add(s)
        c.add(m)

        s = "\\Delta %s = \\sqrt{\\sum_{i} (\\frac{\\partial %s}{\\partial x_i} \\cdot \\Delta x_i)^2}" % (self.eq_symbol, self.eq_symbol)
        if verbose:
            s += f" = {latex(self.gauss_expr)}"
        if self.values:
            s += f" = {self.gauss_delta}"
        c.add(Equation(s))

        if self.values:
            c.add(Equation(f"{self.eq_symbol} = {self.value} \\pm {self.gauss_delta}"))

        return c.latex()


class minmax:
    def __init__(self, expr:Expr, values:dict):
        self.expr = expr
        values = dict(values)

        errors = []
        expr_with_errors = self.expr

        for sym,tup in dict(values).items():
            
            value,error = tup
            
            if error:
                delta = Symbol(f"\\Delta {latex(sym)}")
                errors.append(delta)
                expr_with_errors=expr_with_errors.subs(sym,(sym+delta))
                values[delta] = error
            
            values[sym]=value

        self.value = expr.evalf(subs=values)

        self.min = self.max = self.value
        self.min_expr = self.max_expr = self.expr

        if errors:    

            for combination in product({-1,1},repeat=len(errors)):

                comb_expr = expr_with_errors.subs({delta : a*delta for a,delta in zip(combination,errors)})
                comb_result = comb_expr.evalf(subs=values)
                
                if comb_result < self.min:
                    self.min_expr = comb_expr
                    self.min = comb_result

                if comb_result > self.max:
                    self.max_expr = comb_expr
                    self.max = comb_result

