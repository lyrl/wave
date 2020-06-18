# Form / Toggle
# No description available.
# ---
from telesync import Q, listen, ui


async def main(q: Q):
    if q.args.show_inputs:
        q.page['example'].items = [
            ui.text(f'toggle_unchecked={q.args.toggle_unchecked}'),
            ui.text(f'toggle_checked={q.args.toggle_checked}'),
            ui.text(f'toggle_unchecked_disabled={q.args.toggle_unchecked_disabled}'),
            ui.text(f'toggle_checked_disabled={q.args.toggle_checked_disabled}'),
            ui.button(name='show_form', label='Back', primary=True),
        ]
    else:
        q.page['example'] = ui.form_card(box='1 1 4 10', items=[
            ui.toggle(name='toggle_unchecked', label='Not checked'),
            ui.toggle(name='toggle_checked', label='Checked', value=True),
            ui.toggle(name='toggle_unchecked_disabled', label='Not checked (Disabled)', disabled=True),
            ui.toggle(name='toggle_checked_disabled', label='Checked (Disabled)', value=True, disabled=True),
            ui.button(name='show_inputs', label='Submit', primary=True),
        ])
    await q.page.push()


if __name__ == '__main__':
    listen('/demo', main)