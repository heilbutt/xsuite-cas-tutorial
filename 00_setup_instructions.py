import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Xsuite CAS Hands-On Setup Instructions

    following https://github.com/xsuite/tutorial_cas_nov_2026/blob/main/setup_instructions.md
    """)
    return


@app.cell
def _():
    import marimo as mo
    import xtrack as xt
    import matplotlib.pyplot as plt

    return mo, plt, xt


@app.cell
def _(plt, xt):
    env = xt.Environment()
    env.particle_ref = xt.Particles(p0c=1e9, mass0=xt.PROTON_MASS_EV)

    # Variables and element definitions
    env['kq'] = 0.1
    env.new('qf', xt.Quadrupole, length=1.0, k1='kq')
    env.new('qd', xt.Quadrupole, length=1.0, k1='-kq')
    env.new('d', xt.Drift, length=2.0)

    # Build a FODO cell
    line = env.new_line(name='fodo', components=[
        env.place('qf'), env.place('d'),
        env.place('qd'), env.place('d'),
    ])

    # Plot the twiss
    tw = line.twiss(method='4d')
    tw.plot()

    plt.show()
    return


if __name__ == "__main__":
    app.run()
