Name:		texlive-frletter
Version:	20080819
Release:	1
Summary:	Typeset letters in the French style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/frletter
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frletter.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frletter.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
A small class for typesetting letters in France. No assumption
is made about the language in use. The class represents a small
modification of the beletter class, which is itself a
modification of the standard LaTeX letter class.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/frletter/frletter.cls
%doc %{_texmfdistdir}/doc/latex/frletter/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
