"""citry-bootstrap"""

from collections.abc import Mapping

from citry import Citry, ComponentLibrary, LibraryComponent, LibraryInstallation

from citry_bootstrap.components.bootstrap5.accordion import (
    Accordion,
    AccordionBody,
    AccordionButton,
    AccordionHeader,
    AccordionItem,
)
from citry_bootstrap.components.bootstrap5.alert import Alert, AlertHeading, AlertLink
from citry_bootstrap.components.bootstrap5.badge import Badge
from citry_bootstrap.components.bootstrap5.breadcrumb import Breadcrumb, BreadcrumbItem
from citry_bootstrap.components.bootstrap5.button import Button
from citry_bootstrap.components.bootstrap5.button_group import ButtonGroup, ButtonToolbar
from citry_bootstrap.components.bootstrap5.card import (
    Card,
    CardBody,
    CardFooter,
    CardGroup,
    CardHeader,
    CardImg,
    CardImgOverlay,
    CardLink,
    CardSubtitle,
    CardText,
    CardTitle,
)
from citry_bootstrap.components.bootstrap5.carousel import (
    Carousel,
    CarouselCaption,
    CarouselIndicator,
    CarouselItem,
    CarouselRenderer,
)
from citry_bootstrap.components.bootstrap5.close_button import CloseButton
from citry_bootstrap.components.bootstrap5.collapse import Collapse, CollapseToggle
from citry_bootstrap.components.bootstrap5.dropdown import (
    Dropdown,
    DropdownDivider,
    DropdownHeader,
    DropdownItem,
    DropdownItemText,
    DropdownMenu,
    DropdownToggle,
)
from citry_bootstrap.components.bootstrap5.dropdown_button import DropdownButton, SplitButton
from citry_bootstrap.components.bootstrap5.figure import Figure, FigureCaption, FigureImage
from citry_bootstrap.components.bootstrap5.form import (
    Form,
    FormCheck,
    FormCheckInput,
    FormCheckLabel,
    FormControl,
    FormFloating,
    FormGroup,
    FormLabel,
    FormSelect,
    FormText,
    FormTextarea,
)
from citry_bootstrap.components.bootstrap5.form_range import FormRange
from citry_bootstrap.components.bootstrap5.image import Image
from citry_bootstrap.components.bootstrap5.input_group import (
    FloatingLabel,
    InputGroup,
    InputGroupCheckbox,
    InputGroupRadio,
    InputGroupText,
)
from citry_bootstrap.components.bootstrap5.layout import Col, Container, Row
from citry_bootstrap.components.bootstrap5.list_group import ListGroup, ListGroupItem
from citry_bootstrap.components.bootstrap5.modal import (
    Modal,
    ModalBody,
    ModalFooter,
    ModalHeader,
    ModalTitle,
    ModalToggle,
)
from citry_bootstrap.components.bootstrap5.nav import Nav, NavItem, NavLink
from citry_bootstrap.components.bootstrap5.nav_dropdown import NavDropdown
from citry_bootstrap.components.bootstrap5.navbar import (
    Navbar,
    NavbarBrand,
    NavbarCollapse,
    NavbarNav,
    NavbarText,
    NavbarToggler,
)
from citry_bootstrap.components.bootstrap5.offcanvas import (
    Offcanvas,
    OffcanvasBody,
    OffcanvasHeader,
    OffcanvasTitle,
    OffcanvasToggle,
)
from citry_bootstrap.components.bootstrap5.pagination import (
    PageLink,
    Pagination,
    PaginationEllipsis,
    PaginationFirst,
    PaginationItem,
    PaginationLast,
    PaginationNext,
    PaginationPrev,
)
from citry_bootstrap.components.bootstrap5.placeholder import Placeholder, PlaceholderButton
from citry_bootstrap.components.bootstrap5.popover import Popover
from citry_bootstrap.components.bootstrap5.progress import Progress, ProgressBar, ProgressStacked
from citry_bootstrap.components.bootstrap5.spinner import Spinner
from citry_bootstrap.components.bootstrap5.stack import Stack
from citry_bootstrap.components.bootstrap5.table import Table
from citry_bootstrap.components.bootstrap5.tabs import (
    Tab,
    TabContainer,
    TabContent,
    TabPane,
    Tabs,
    TabsRenderer,
)
from citry_bootstrap.components.bootstrap5.toast import (
    Toast,
    ToastBody,
    ToastContainer,
    ToastHeader,
)
from citry_bootstrap.components.bootstrap5.toggle_button import ToggleButton, ToggleButtonGroup
from citry_bootstrap.components.bootstrap5.tooltip import Tooltip
from citry_bootstrap.plain_inputs import PlainInputs

#: Every component is published under this prefix; `install(alias=...)` adds more.
PREFIX = "bs-"

__citry_library__ = ComponentLibrary(
    name="citry-bootstrap",
    required_extensions=("plain_inputs",),
    components=(
        Accordion,
        AccordionItem,
        AccordionButton,
        AccordionHeader,
        AccordionBody,
        Alert,
        AlertLink,
        AlertHeading,
        Badge,
        Breadcrumb,
        BreadcrumbItem,
        Button,
        ButtonGroup,
        ButtonToolbar,
        Card,
        CardHeader,
        CardBody,
        CardFooter,
        CardTitle,
        CardSubtitle,
        CardText,
        CardLink,
        CardImg,
        CardImgOverlay,
        CardGroup,
        Carousel,
        CarouselRenderer,
        CarouselItem,
        CarouselCaption,
        CarouselIndicator,
        CloseButton,
        Collapse,
        CollapseToggle,
        Dropdown,
        DropdownToggle,
        DropdownMenu,
        DropdownItem,
        DropdownDivider,
        DropdownHeader,
        DropdownItemText,
        DropdownButton,
        SplitButton,
        Figure,
        FigureImage,
        FigureCaption,
        Form,
        FormGroup,
        FormLabel,
        FormControl,
        FormTextarea,
        FormSelect,
        FormCheckInput,
        FormCheckLabel,
        FormCheck,
        FormText,
        FormFloating,
        FormRange,
        Image,
        InputGroup,
        InputGroupText,
        InputGroupRadio,
        InputGroupCheckbox,
        FloatingLabel,
        Container,
        Row,
        Col,
        ListGroup,
        ListGroupItem,
        Modal,
        ModalHeader,
        ModalBody,
        ModalFooter,
        ModalTitle,
        ModalToggle,
        Nav,
        NavItem,
        NavLink,
        NavDropdown,
        Navbar,
        NavbarBrand,
        NavbarToggler,
        NavbarCollapse,
        NavbarNav,
        NavbarText,
        Offcanvas,
        OffcanvasHeader,
        OffcanvasBody,
        OffcanvasTitle,
        OffcanvasToggle,
        Pagination,
        PaginationItem,
        PageLink,
        PaginationFirst,
        PaginationPrev,
        PaginationNext,
        PaginationLast,
        PaginationEllipsis,
        Placeholder,
        PlaceholderButton,
        Popover,
        Progress,
        ProgressStacked,
        ProgressBar,
        Spinner,
        Stack,
        Table,
        TabContainer,
        TabContent,
        TabPane,
        TabsRenderer,
        Tabs,
        Tab,
        ToastContainer,
        Toast,
        ToastHeader,
        ToastBody,
        ToggleButtonGroup,
        ToggleButton,
        Tooltip,
    ),
)


def _republished(
    component: type[LibraryComponent], prefix: str, override: "Mapping[type, type]"
) -> type[LibraryComponent]:
    """One component under `prefix`, with its sibling references following."""
    definition = override.get(component, component)
    name = prefix + component.name.removeprefix(PREFIX)
    changes: dict[str, object] = {"name": name}
    template = getattr(definition, "template", None)
    if isinstance(template, str) and f"<c-{PREFIX}" in template:
        changes["template"] = template.replace(f"<c-{PREFIX}", f"<c-{prefix}").replace(
            f"</c-{PREFIX}", f"</c-{prefix}"
        )
    return type(definition.__name__, (definition,), changes)


def library(
    *, prefix: str = PREFIX, override: "Mapping[type, type] | None" = None
) -> ComponentLibrary:
    """The manifest, published under `prefix`, with components replaced.

    A component's template names its siblings, so the prefix is rewritten in
    both places at once. Nothing is published under the old prefix afterwards.
    """
    override = dict(override or {})
    unknown = set(override) - set(__citry_library__.components)
    if unknown:
        names = ", ".join(sorted(c.__name__ for c in unknown))
        msg = f"not part of this library: {names}"
        raise ValueError(msg)
    if prefix == PREFIX and not override:
        return __citry_library__
    return ComponentLibrary(
        name="citry-bootstrap",
        required_extensions=("plain_inputs",),
        components=tuple(_republished(c, prefix, override) for c in __citry_library__.components),
    )


def install(
    app: Citry, *, prefix: str = PREFIX, override: "Mapping[type, type] | None" = None
) -> LibraryInstallation:
    """Register the library.

    Components are published as `<c-bs-button>`. `prefix` changes that for all
    of them - `prefix=""` gives `<c-button>` - and `override` swaps one for your
    own subclass, which every sibling then renders too:

        install(app, prefix="ui-", override={CardBody: MyCardBody})
    """
    return app.register_library(library(prefix=prefix, override=override))


__all__ = [
    "install",
    "__citry_library__",
    "PlainInputs",
    "Accordion",
    "AccordionItem",
    "AccordionButton",
    "AccordionHeader",
    "AccordionBody",
    "Alert",
    "AlertLink",
    "AlertHeading",
    "Badge",
    "Breadcrumb",
    "BreadcrumbItem",
    "Button",
    "ButtonGroup",
    "ButtonToolbar",
    "Card",
    "CardHeader",
    "CardBody",
    "CardFooter",
    "CardTitle",
    "CardSubtitle",
    "CardText",
    "CardLink",
    "CardImg",
    "CardImgOverlay",
    "CardGroup",
    "Carousel",
    "CarouselRenderer",
    "CarouselItem",
    "CarouselCaption",
    "CarouselIndicator",
    "CloseButton",
    "Collapse",
    "CollapseToggle",
    "Dropdown",
    "DropdownToggle",
    "DropdownMenu",
    "DropdownItem",
    "DropdownDivider",
    "DropdownHeader",
    "DropdownItemText",
    "DropdownButton",
    "SplitButton",
    "Figure",
    "FigureImage",
    "FigureCaption",
    "Form",
    "FormGroup",
    "FormLabel",
    "FormControl",
    "FormTextarea",
    "FormSelect",
    "FormCheckInput",
    "FormCheckLabel",
    "FormCheck",
    "FormText",
    "FormFloating",
    "FormRange",
    "Image",
    "InputGroup",
    "InputGroupText",
    "InputGroupRadio",
    "InputGroupCheckbox",
    "FloatingLabel",
    "Container",
    "Row",
    "Col",
    "ListGroup",
    "ListGroupItem",
    "Modal",
    "ModalHeader",
    "ModalBody",
    "ModalFooter",
    "ModalTitle",
    "ModalToggle",
    "Nav",
    "NavItem",
    "NavLink",
    "NavDropdown",
    "Navbar",
    "NavbarBrand",
    "NavbarToggler",
    "NavbarCollapse",
    "NavbarNav",
    "NavbarText",
    "Offcanvas",
    "OffcanvasHeader",
    "OffcanvasBody",
    "OffcanvasTitle",
    "OffcanvasToggle",
    "Pagination",
    "PaginationItem",
    "PageLink",
    "PaginationFirst",
    "PaginationPrev",
    "PaginationNext",
    "PaginationLast",
    "PaginationEllipsis",
    "Placeholder",
    "PlaceholderButton",
    "Popover",
    "Progress",
    "ProgressStacked",
    "ProgressBar",
    "Spinner",
    "Stack",
    "Table",
    "TabContainer",
    "TabContent",
    "TabPane",
    "TabsRenderer",
    "Tabs",
    "Tab",
    "ToastContainer",
    "Toast",
    "ToastHeader",
    "ToastBody",
    "ToggleButtonGroup",
    "ToggleButton",
    "Tooltip",
]
