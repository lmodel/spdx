package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A reference to a resource identifier defined outside the scope of SPDX-3.0 content that uniquely identifies an Element.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExternalIdentifier  {

  private String type;
  private String comment;
  private String externalIdentifierType;
  private String identifier;
  private List<URI> identifierLocator;
  private String issuingAuthority;


}