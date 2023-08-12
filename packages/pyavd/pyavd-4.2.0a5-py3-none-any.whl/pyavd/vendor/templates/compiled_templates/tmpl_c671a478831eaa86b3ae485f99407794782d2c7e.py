from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos-device-documentation.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_eos_cli_config_gen_documentation = resolve('eos_cli_config_gen_documentation')
    l_0_hostname = resolve('hostname')
    l_0_inventory_hostname = resolve('inventory_hostname')
    l_0_hide_passwords = missing
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    pass
    l_0_hide_passwords = t_1(environment.getattr((undefined(name='eos_cli_config_gen_documentation') if l_0_eos_cli_config_gen_documentation is missing else l_0_eos_cli_config_gen_documentation), 'hide_passwords'), True)
    context.vars['hide_passwords'] = l_0_hide_passwords
    context.exported_vars.add('hide_passwords')
    yield '# '
    yield str(t_1((undefined(name='hostname') if l_0_hostname is missing else l_0_hostname), (undefined(name='inventory_hostname') if l_0_inventory_hostname is missing else l_0_inventory_hostname)))
    yield '\n\n## Table of Contents\n\n<!-- toc -->\n<!-- toc -->\n'
    template = environment.get_template('documentation/management.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/cvx.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/authentication.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/address-locking.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/management-security.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/prompt.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/aliases.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/dhcp-relay.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/boot.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/monitoring.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/monitor-connectivity.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/tcam-profile.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/link-tracking-groups.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/mlag-configuration.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/lldp.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/l2-protocol-forwarding.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/lacp.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/spanning-tree.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/vlan-internal-order.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/vlans.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/mac-address-table.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/interfaces.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/routing.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/bfd.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/mpls.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/patch-panel.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/multicast.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/filters.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/dot1x.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/poe.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/acl.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/vrfs.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/virtual-source-nat-vrfs.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/platform.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/router-l2-vpn.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/ip-dhcp-relay.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/ip-nat.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/errdisable.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/mac-security.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/traffic-policies.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/quality-of-service.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/maintenance-mode.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/eos-cli.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event
    template = environment.get_template('documentation/custom-templates.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'hide_passwords': l_0_hide_passwords})):
        yield event

blocks = {}
debug_info = '2=21&3=25&10=27&12=30&14=33&16=36&18=39&20=42&22=45&24=48&26=51&28=54&30=57&32=60&34=63&36=66&38=69&40=72&42=75&44=78&46=81&48=84&50=87&52=90&54=93&56=96&58=99&60=102&62=105&64=108&66=111&68=114&70=117&72=120&74=123&76=126&78=129&80=132&82=135&84=138&86=141&88=144&90=147&92=150&94=153&96=156'